__author__ = 'ravi'

s = r"""
    1
   2\t2
  3 {} 3
   4 4
    5
""".format('x')

print '-' * 5
print s.rstrip('\n')
print '-' * 5