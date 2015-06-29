__author__ = 'ravi'
"""
local
global
builtins
"""
n = None

def demo():

    n = 'pypi'  #local to the function demo
    global n
    print n

demo()
print n

print __name__
print __file__


