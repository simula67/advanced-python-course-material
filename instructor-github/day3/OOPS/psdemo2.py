__author__ = 'ravi'

class Demo(object):
    addr1 = "testit"

    def __del__(self):
        #print "{}: destroying the object".format(self)
        pass

    def get_data(self):
        return self.data

    def __init__(self, data=None):
        self.data = data
        self.addr = None
        #print "{}: in the constructor".format(self)

if __name__ == '__main__':
    Demo.addr1 = "peter pan"
    d = Demo(100)

