__author__ = 'ravi'

l = [1, 2, 'three', 4.0, 5+0j]
l.append('hp')
l.insert(0, 'bangalore')

print l

value = l.pop(0)
print value
print l

del l[2]
print l