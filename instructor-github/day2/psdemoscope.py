__author__ = 'ravi'
"""
local
global
builtins
"""
n = 100  #global scope

def demo2(arg):
    arg.append('peter pan')

def demo():
    n = []  #local to the function demo
    demo2(n)
    print n



demo()
#print n


