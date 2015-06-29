__author__ = 'ravi'
import re

s = 'the python scripting'
pattern = 'PythoN'

m = re.search(pattern, s, re.I)

if m:
    print m.group()
    print m.start()
    print m.end()
    print m.span()
else:
    print "failed to match :("
