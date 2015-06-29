__author__ = 'ravi'
from math import  ceil

def center(content, width, fill=" "):
    n_times = (width - len(content)) / 2.0
    lhs = int(ceil(n_times))
    return "{}{}{}".format(fill * lhs, content,
                           fill * int(n_times))

print "perl".center(9, '-')
print center('perl', 9, '-')

