__author__ = 'ravi'
import re
s = 'this is a sample string'
counter = 0

def nth_replace(m):
    global counter
    counter += 1
    return '*' if counter == 4  else m.groups()[0]

print re.sub(r'([AEIOU])', nth_replace, s, flags=re.I)