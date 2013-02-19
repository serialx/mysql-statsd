from vars import *
import os
import copy
import sys
import re

class Gather(object):
    """Object to gather OS metrics"""
    def __init__(self, logger):
        self.logger = logger

    def collect(self):
        '''
        Here the correct calls are made to collect the different stats from the operating system
        '''
        self.results = copy.deepcopy(os_varaibles)
        self.load()
        self.memory()
        return self.results

    def load(self):
        load = os.getloadavg()
        self.results['1minload'][1] = round(load[0], 1)
        self.results['5minload'][1] = round(load[1], 1)
        self.results['15minload'][1] = round(load[2], 1)
        return

    def memory(self):
        meminfo = []
        lines = open("/proc/meminfo", "r")
        for line in lines:
            value = self.row_float(line)
            meminfo.append(value)
        lines.close()
        self.results['memtotal'][1] = int(meminfo[0])
        self.results['freemem'][1] = int(meminfo[1])
        self.results['usedmem'][1] = int(meminfo[0]) - int(meminfo[1])
        self.results['swaptotal'][1] = int(meminfo[13])
        self.results['swapfree'][1] = int(meminfo[14])
        self.results['usedswap'][1] = int(meminfo[13]) - int(meminfo[14])
        return


    def row_float(self, row):
        '''
        Finds all the floats in a string and returns a list.
        '''
        floats = re.findall(r"[-+]?\d*\.\d+|\d+", row)
        return floats[0]
