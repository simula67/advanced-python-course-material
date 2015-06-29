__author__ = 'ravi'
import re

g = (l for l in open('/etc/passwd') if re.search(r'a', l))
l = [l for l in open('/etc/passwd') if re.search(r'a', l)]

"""
print g.__sizeof__()
print l.__sizeof__()

for item in g:
    print item,
"""