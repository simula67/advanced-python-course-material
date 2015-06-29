__author__ = 'ravi'

class Demo(object):
    pass

if __name__ == '__main__':
    d = Demo()
    d.name = 'hp'
    d.city = 'ca'
    #print dir(d)
    print d.__dict__

    """
    print type(d)
    print d.__class__
    print d.__class__.__name__
    """



