__author__ = 'antonjoj'

import re

counter = 0

# Capture and replace nth

def nth_replace(m):
    global counter
    counter += 1
    return '*' if counter == 4 else m.groups()[0]

print re.sub(r'([aeiou])', nth_replace, "this is a string", flags=re.I)