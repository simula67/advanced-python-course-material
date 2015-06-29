__author__ = 'antonjoj'

class Box(object):

    def __init__(self, size,length):
        self.size= size
        self.length = length

    def __add__(self, other):
        if type(other) is int:
            return other + self.size
        else:
            return Box(other.size + self.size, other.length + self.size)

    def __mul__(self, other):
        if type(other) is int:
            return other * self.size
        else:
            return Box(other.size * self.size, other.length * self.size)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.size == other.size

    __radd__ = __add__

    def __str__(self):
        return "Stringify : {} {}".format(self.size, self.length)

if __name__ == '__main__':

    box = Box(10, 2)
    print box + 4
    print 4 + box  # Will invoke radd
    print box


