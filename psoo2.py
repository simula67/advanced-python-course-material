__author__ = 'antonjoj'
class Demo(object):
    stat = "test"
    def __init__(self, data):
        self.data = data
        print "{}: in the constructor".format(self)

    def __del__(self):
        print "{} destroying the object".format(self)

if __name__ == '__main__':
    d = Demo(23)
    print d.stat
    Demo.stat = "test2"
    print d.stat
    d.stat = 12
    print d
    print d.data
    print d.__dict__