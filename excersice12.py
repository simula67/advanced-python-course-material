__author__ = 'antonjoj'

from collections import deque

# write functions that behave like head and tail
# count and order

def head(fp, count):
    index = 1
    for line in fp:
        if index > count:
            break
        index += 1
        print line,


def tail(fp, count):
    for i in deque(fp, count):
        print i,

def headntail(filename, **param):
    order = param.get('order', "head")
    count = param.get('count', 10)
    fp = open(filename).readlines()
    if order == "head":
        head(fp, count)
    elif order == "tail":
        tail(fp, count)
    else:
        print "order should be either head or tail"


headntail("datafiles\\passwd", order="head", count=12)

