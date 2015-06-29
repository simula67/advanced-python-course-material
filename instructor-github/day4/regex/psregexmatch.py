__author__ = 'ravi'
import re

s = 'the python scripting'
pattern = 'PythoN'

m = re.match(pattern, s, re.I)

if m:
    print m
    print "we got a match :)"
else:
    print "failed to match :("
