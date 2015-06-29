__author__ = 'ravi'
import re
import fileinput

c = re.compile(r'(\d+)')

for line in fileinput.input(inplace=True, backup='.bak'):
    if fileinput.lineno() % 2:
        print c.sub(r'[\1]', line),
    else:
        print line,

