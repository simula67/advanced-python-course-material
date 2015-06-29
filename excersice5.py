__author__ = 'antonjoj'

from pprint import pprint

content = [('blue', 2), ('yellow', 3), ('blue', 4), ('red', 3), ('red', 10)]
info = {}
for color, value in content:
    info.setdefault(color, []).append(value)

pprint(info)