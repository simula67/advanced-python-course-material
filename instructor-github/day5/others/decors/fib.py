def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def trace(f):
    def g(x):
        print f.__name__, x
        value = f(x)
        print 'return', repr(value)
        return value
    return g

fib = trace(fib)
print fib(3)
