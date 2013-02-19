import logging
import argparse
import ConfigParser
import os
import sys
import socket
import MySQLdb
import statsd
import time
import mysqlstats
import osstats
from twisted.internet.task import LoopingCall
from twisted.internet import reactor


def main(settings, logger):

    try:
        logger.info('Attempting to connect to MySQL on: {0}'.format(settings['host']))
        mysql_conn = MySQLdb.connect(host=settings['host'], user=settings['user'],
                      passwd=settings['password'])
        mysql_cursor = mysql_conn.cursor()
        logger.info('Connection to MySQL on {0} sucessful'.format(settings['host']))

    except MySQLdb.OperationalError:
        logger.critical('Cannot connect to {0}'.format(settings['host']))
        time.sleep(5)
        sys.exit()

    prefix = '{0}.{1}'.format(settings['prefix'], socket.gethostname().replace('.', '-'))
    stats = statsd.StatsClient(settings['statsd_host'], settings['statsd_port'], prefix=prefix, batch_len=10000)
    gather = mysqlstats.Gather(mysql_cursor, stats, logger, settings)
    os_gather = osstats.Gather(logger)

    def stats_count(stat, value, prefix):
        '''
        Increment a statsd counter
        '''
        stats.incr('{0}.{1}'.format(prefix, stat), value)

    def stats_timer(stat, value, prefix):
        '''
        Make a statsd timer call
        '''
        stats.timer('{0}.{1}'.format(prefix, stat), value)

    def stats_gauge(stat, value, prefix):
        '''
        Make a guage statsd call
        '''
        stats.gauge('{0}.{1}'.format(prefix, stat), value)

    calls = {
        'gauge': stats_gauge,
        'count': stats_count,
        'timer': stats_timer
        }

    def collect():
        osresults = os_gather.collect()
        for result in osresults:
            statsd_call = calls[osresults[result][0]]
            statsd_call(result, osresults[result][1], 'os')


        results = gather.collect()
        if results['connected']:
            for result in results['mysql_vars']:
                statsd_call = calls[results['mysql_vars'][result][0]]
                statsd_call(result, results['mysql_vars'][result][1], 'mysql')
            stats.flush()
            return
        elif not results['connected']:
            for result in results['mysql_vars']:
                statsd_call = calls[results['mysql_vars'][result][0]]
                statsd_call(result, 0, 'mysql')
            stats.flush()
            reactor.callFromThread(reactor.stop)
        else:
            logger.critical('Something is wrong.... Shutting down - see logs for errors')
            reactor.callFromThread(reactor.stop)


    loop = LoopingCall(collect)
    loop.start(int(settings['interval']))
    reactor.run()
    logger.warn('Connection to MySQL lost. Shutting down.')


def validate_config(config_file):
    # Takes the location of the config file, sets some defualts and then parses the ini options
    config = ConfigParser.RawConfigParser({'prefix': ''})
    config.read(config_file)
    config_dict = {}
    config_dict['interval'] = config.get('general', 'poll_interval')
    config_dict['prefix'] = config.get('general', 'prefix')
    config_dict['host'] = config.get('mysql', 'host')
    config_dict['user'] = config.get('mysql', 'user')
    config_dict['password'] = config.get('mysql', 'password')
    config_dict['long_query_time'] = config.get('mysql', 'long_query_time')
    config_dict['statsd_host'] = config.get('statsd', 'host')
    config_dict['statsd_port'] = config.getint('statsd', 'port')
    return config_dict


def create_logger_object():
    # If a logfile exists the the logging will be sent there if not it will go to stout unbuffered.
    logger = logging.getLogger("MySQL Statsd")
    level = getattr(logging, args.loglevel.upper())
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    if args.logfile:
        fh = logging.FileHandler(args.logfile)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    else:
        sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
        console = logging.StreamHandler(sys.stdout)
        logger.addHandler(console)
    return logger

if __name__ == '__main__':

    # Parse the supplied command line arguements and provide help
    parser = argparse.ArgumentParser(description='Collect MySQL variables and push them to Statsd.')
    parser.add_argument("--config",
                        help="Specify config file.", metavar="CONFIG_FILE", required=True)
    parser.add_argument("--logfile",
                        help="Specify a log file.", metavar="LOG_FILE")
    parser.add_argument("--loglevel",
                        help="What level would you like to log at? INFO, DEBUG, WARN", metavar="LOG_LEVEL", default="INFO")
    args = parser.parse_args()

    # Create a logging object
    logger = create_logger_object()
    logger.info('Starting MySQL-statsd')

    # If the config file does not exist log and throw an error
    if not os.path.exists(args.config):
        logger.warn('{0} Exiting'.format(args.config))
        raise IOError('Specified config file does not exist.')
        sys.exit()
    # Validate the supplied config
    settings = validate_config(args.config)

    main(settings, logger)
