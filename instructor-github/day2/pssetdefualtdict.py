__author__ = 'ravi'
from pprint import pprint
info = {}

content = [('blue', 4), ('yellow', 3), ('blue', 2),
           ('red', 2), ('red', 10)]

for color, value in content:

    info.setdefault(color, ['x']).append(value)
    #info.setdefault(color, )
    #print info

print
pprint(info)



