__author__ = 'antonjoj'
# write grep

import fileinput
from sys import argv
import re


try:
    global pattern
    pattern = argv.pop(1)
except IndexError, e:
    print "Usage : {} pattern [filename1] [filename2] etc".format(argv[0])
    exit(1)

for line in fileinput.input():
    if re.search(pattern, line, re.I):
        print line,