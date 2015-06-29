__author__ = 'antonjoj'

import re

s = "the python scripting"
pattern = "python"
#search will find the pattern anywhere in the string
m = re.search(pattern, s, re.I)
if m:
    print m.group()
    print m.start()
    print m.end()
    print m.span()