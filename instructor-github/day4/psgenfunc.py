__author__ = 'ravi'

def demo():
    print "before y1"
    yield 'one'
    print "after y1"
    print "before y2"
    yield 2
    print "after y2"
"""
for i in demo():
    print i
    print '-' * 5
"""

g = demo()
print g.next()
print '-' * 5
print g.next()
print '-' * 5
print g.next()
