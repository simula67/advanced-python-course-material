__author__ = 'ravi'
import re
from fileinput import input
from sys import argv

class GrepMe(object):
    def __init__(self, pattern):
        self.pattern = pattern
        self.__do_grep()

    def __do_grep(self):
        for line in input():
            if re.search(self.pattern, line):
                print line,

if __name__ == '__main__':
    GrepMe(argv.pop(1))

