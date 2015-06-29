__author__ = 'antonjoj'

def demo(*args):
    #args is tuple
    print args

demo()
demo(1,2,3)

demo('pter pan')

l = [1,2,3,4]
t = (1,2,3)

demo(l)
demo(t)

demo(*l)
demo(*t)
