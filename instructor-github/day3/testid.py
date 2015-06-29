__author__ = 'ravi'

s = [1,2,3,4]
t = [1,2,3,4]

#shallow copy vs deepcopy

bup = t
del t[0]
print bup
print t
