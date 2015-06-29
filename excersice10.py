__author__ = 'antonjoj'


def mymap( callback, seq):
    return [callback(i) for i in seq]

print map(str, range(1,5))
print mymap(str, range(1,5))

def myfilter(callback, seq):
    return [i for i in seq if callback(i)]

print filter(lambda x: x%7 == 0, range(100))
print myfilter(lambda x: x%7 == 0, range(100))
