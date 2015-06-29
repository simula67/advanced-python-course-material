__author__ = 'ravi'

def demo(*args):
    print args

demo()
demo(121)
demo('peter pan')
demo(1,2,3,4, 'cpan', 'gems', 'pypi')
l = [1,2,'3',4]
t = ('perl', 'pypi')
demo(*l)
demo(*t)