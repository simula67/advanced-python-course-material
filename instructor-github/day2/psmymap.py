__author__ = 'ravi'

def mymap(callback, seq):
    return [callback(i) for i in seq]

print map(str, range(1, 5))
print mymap(lambda i: "<td>{}</td>".format(i), range(1, 5))
