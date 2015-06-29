__author__ = 'ravi'

def demo(stop):
    i = 0
    print "entering while loop"
    while i < stop:
        print "before : {}".format(i)
        yield i
        i += 1
        print "after : {}".format(i)

#print demo(4)
for item in demo(6):
    print item
