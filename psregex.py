__author__ = 'antonjoj'

import re

s = "python scripting"
matching_pattern = "python"
non_matching_pattern = "PYTHON"

# Match will only match the beginning of the list
m1 = re.match(matching_pattern, s)
if m1:
    print m1
    print "we got a match"
else:
    print "failed to match"

m2 = re.match(non_matching_pattern, s)
if m2:
    print m2
    print "we got a match"
else:
    print "failed to match"
