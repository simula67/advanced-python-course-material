__author__ = 'antonjoj'
from copy import deepcopy

s = [1,2,3,4]
shallow_copy_of_s = s

shallow_copy_of_s.pop()
print shallow_copy_of_s
print s

deep_copy_of_s = deepcopy(s)

s.pop()
print s
print deep_copy_of_s
