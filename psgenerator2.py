__author__ = 'antonjoj'

import re

def grepit(filename, pattern):
    for line in open(filename):
        if re.search(pattern, line):
            yield line


for i in grepit("datafiles\\passwd", "root"):
    print i,

