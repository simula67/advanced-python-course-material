__author__ = 'ravi'

def my_filter(callback, seq):
    return [i for i in seq if callback(i)]

l = range(50)
print filter(lambda v: v%7==0, l)

print my_filter(lambda v: v%7==0, l)

