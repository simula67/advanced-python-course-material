__author__ = 'ravi'
class Zero(object):
    def pprint(self):
        print "pprint from the class Zero"

class A(Zero):
    def pprint(self):
        print "pprint from the class A"

class B(object):
    def pprint(self):
        print "pprint from the class B"

class C(B, A):
    def pprint(self):
        super(A, self).pprint()

if __name__ == '__main__':
    C().pprint()
