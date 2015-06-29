__author__ = 'antonjoj'

class A(object):
    def pprint(self):
        print "pprint from the class A"

class B(object):
    def pprint(self):
        print "pprint from the class B"

class C(A,B):
    def pprint(self):
        #super(C,self).pprint()
        A.pprint(self)
        B.pprint(self)

if __name__ == '__main__':
    C().pprint()

