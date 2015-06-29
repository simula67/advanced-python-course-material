__author__ = 'antonjoj'

n = 10
m = 11

def demo():
    global n
    m = 12
    print n
    print m

demo()

#special variable
print __file__
