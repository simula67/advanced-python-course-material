__author__ = 'ravi'
from copy import deepcopy

s = [1,2,3,4]
copy_of_s = deepcopy(s)

print id(s)
print id(copy_of_s)

s.pop()
print s
print copy_of_s