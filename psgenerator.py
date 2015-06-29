__author__ = 'antonjoj'


import re
g = (l for l in open("datafiles\\passwd") if re.search(r'^a', l))

print g
print g.next(),
print g.next(),


print "Going into for each"
for i in g:
    print i