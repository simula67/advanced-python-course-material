__author__ = 'ravi'
import re

s = 'this is a sample string'
pattern = re.compile(r'([AEIOU])', re.I)
counter = 0

def nth_replace(m):
    global counter
    counter += 1
    return '*' if counter == 4  else m.groups()[0]

print pattern.sub(nth_replace, s)