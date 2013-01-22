from vars import *
import re
import MySQLdb

class Gather(object):

    def __init__(self, mysql_cur, statsd, logger):
        self.mysql_cur = mysql_cur
        self.statsd = statsd
        self.logger = logger
        self.log_permissions = 0


    def collect(self):
        '''
        Here the correct calls are made to collect the different sets of information from the mysql server
        '''
        if self.show_status() is False:
            return False
        if self.slave_status() is False:
            return False
        if self.show_engine_status() is False:
            return False
        return True


    def show_status(self):
        '''
        Here the global status output is read and the variables are matched with the dictionary
        from vars.py to determine which type of graphs should be used.
        Statsd calls are added to the statsd buffer.
        '''
        query = 'SHOW GLOBAL STATUS'
        try:
            self.mysql_cur.execute(query)
            self.mysql_status = self.mysql_cur.fetchall()
        except self.mysql_cur.OperationalError:
            return self.db_error(query)

        for stat in self.mysql_status:
            if stat[0] in show_status:
                calls = {
                'gauge': self.stats_gauge,
                'count': self.stats_count,
                'timer': self.stats_timer
                }
                statsd_call = calls[show_status[stat[0]]]
                statsd_call(stat[0], stat[1])

        return


    def show_engine_status(self):
        '''
        Here we parse the show engine innodb status. Due to the output format we have to do a lot of
        ifs to check the output and then some calculations to get sensible data.
        Alot of this parsing is heavily influenced by the percona cacti graphs.
        Statsd calls are added to the statsd buffer.
        '''
        query = 'SHOW /*!50000 ENGINE*/ INNODB STATUS'
        try:
            self.mysql_cur.execute(query)
            self.mysql_engine_status = self.mysql_cur.fetchall()
        except self.mysql_cur.OperationalError:
            return self.db_error(query)

        self.engine_status = self.mysql_engine_status[0][2]
        transactions_value = 0
        current_transactions = 0
        active_transactions = 0
        innodb_lock_wait_secs = 0
        trx_recorded = False

        for row in self.engine_status.split('\n'):
            if 'Mutex spin waits' in row:
                floats = self.row_float(row)
                self.stats_gauge('mutex_spin_waits', floats[0])
                self.stats_gauge('mutex_spin_rounds', floats[1])
                self.stats_gauge('mutex_spin_oswaits', floats[2])
                continue

            elif 'RW-shared spins' in row and 'RW-excl' in row:
                floats = self.row_float(row)
                self.stats_gauge('rw_shared_spin_waits', floats[0])
                self.stats_gauge('rw_shared_os_waits', floats[1])
                self.stats_gauge('rw_excl_spin_waits', floats[2])
                self.stats_gauge('rw_excl_os_waits', floats[3])
                continue

            elif 'RW-shared spins' in row:
                floats = self.row_float(row)
                self.stats_gauge('rw_shared_spin_waits', floats[0])
                self.stats_gauge('rw_shared_os_waits', floats[1])
                continue

            elif 'RW-excl' in row:
                floats = self.row_float(row)
                self.stats_gauge('rw_excl_spin_waits', floats[0])
                self.stats_gauge('rw_excl_os_waits', floats[1])
                continue

            elif 'Trx id counter' in row:
                split_row = row.split()
                if len(split_row) == 5:
                    transactions_value = (int(split_row[3]) * 4294967296) + int(split_row[4])
                else:
                    transactions_value = int(split_row[3], 16)
                trx_recorded = True
                self.stats_gauge('innodb_transactions', transactions_value)
                continue

            elif 'Purge done for trx' in row:
                split_row = row.split()
                if split_row[7] == 'undo':
                    purge = int(split_row[6], 16)
                    self.stats_gauge('unpurged_transactions', (transactions_value - purge))
                else:
                    purge = (int(split_row[6]) * 4294967296) + int(split_row[7])
                    self.stats_gauge('unpurged_transactions', (transactions_value - purge))
                continue

            elif 'History list length' in row:
                floats = self.row_float(row)
                self.stats_gauge('history_list_length', floats[0])
                continue

            elif trx_recorded and '---TRANSACTION' in row:
                current_transactions += 1
                if 'ACTIVE' in row:
                    active_transactions +=1

            elif trx_recorded and '------- TRX HAS BEEN' in row:
                floats = self.row_float(row)
                innodb_lock_wait_secs += floats[0]

            elif 'read views open inside InnoDB' in row:
                floats = self.row_float(row)
                self.stats_gauge('read_views', floats[0])

        self.stats_gauge('current_transactions', current_transactions)
        self.stats_gauge('active_transactions', active_transactions)
        self.stats_gauge('innodb_lock_wait_secs', innodb_lock_wait_secs)

        return


    def slave_status(self):
        '''
        Here we parse the output of show slave status.
        Statsd calls are added to the statsd buffer.
        '''
        query = 'SHOW SLAVE STATUS'
        try:
            self.mysql_cur.execute(query)
            mysql_slave_status = self.mysql_cur.fetchone()
        except self.mysql_cur.OperationalError:
            return self.db_error(query)

        if mysql_slave_status is None:
            self.stats_gauge('slave_running', 0)
            return

        if mysql_slave_status[11] == 'No':
            self.stats_gauge('slave_io_running', 0)
        else:
            self.stats_gauge('slave_io_running', 1)

        if mysql_slave_status[12] == 'No':
            self.stats_gauge('slave_sql_running', 0)
        else:
            self.stats_gauge('slave_sql_running', 1)
        
        if mysql_slave_status[32]:
            self.stats_gauge('seconds_behind_master', mysql_slave_status[32])
        else:
            self.stats_gauge('seconds_behind_master', 0)

        self.stats_gauge('relay_log_space', mysql_slave_status[22])

        return


    def zero_stats(self):
        '''
        If there is no connection to MySQL we zero the stats and buffer them.
        '''
        # Show status is a list of show status variables imported from vars.py
        for stat in show_status:
            calls = {
            'gauge': self.stats_gauge,
            'count': self.stats_count,
            'timer': self.stats_timer
            }
            statsd_call = calls[show_status[stat]]
            statsd_call(stat, 0)
        return

    def db_error(self, query):
        '''
        This function deals with database exceptions. It checks if the connection is still alive.
        If the connection is alive but the there are still problems running queries it warns about permission errors.
        This function also calls zeros_stats based on certain criteria.
        '''
        try:
            test_query = 'SELECT current_user()'
            self.mysql_cur.execute(test_query)
        except self.mysql_cur.OperationalError:
            self.logger.warn('Unable to query MySQL')
            self.zero_stats()
            return False

        if self.log_permissions < 2:
            self.logger.warn('Unable to execute: {0} - Check user permissions'.format(query))
            self.log_permissions += 1
        return True


    def stats_count(self, stat, value):
        '''
        Increment a statsd counter 
        '''
        self.statsd.incr('mysql.{0}'.format(stat), value)


    def stats_timer(self, stat, value):
        '''
        Make a statsd timer call
        '''
        self.statsd.timer('mysql.{0}'.format(stat), value)


    def stats_gauge(self, stat, value):
        '''
        Make a guage statsd call
        '''
        self.statsd.gauge('mysql.{0}'.format(stat), value)


    def row_float(self, row):
        '''
        Finds all the floats in a string and returns a list.
        '''
        floats = re.findall(r"[-+]?\d*\.\d+|\d+", row)
        return floats


    def send(self):
        '''
        Takes the buffered statsd calls and sends them to the statsd host.
        '''
        self.statsd.flush()
