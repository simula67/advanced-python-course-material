__author__ = 'antonjoj'

import re

l = ["12.21", "51.34", "11.11"]

# backreferences

for i in l:
    if re.match(r'(\d)(\d)\.\2\1', i):
        print i