__author__ = 'ravi'

class Box(object):
    def __init__(self, size, length=0):
        self.size = size
        self.length = length

    def __eq__(self, other):
        return self.size == other.size

    def __mul__(self, other):   # a * 3
        if type(other) in [int, float]:
            return Box(self.size * other)
        elif type(other) is Box:
            return Box(self.size * other.size)

    __rmul__ = __mul__

    def __add__(self, other):   # a + 3
        if type(other) in [int, float]:
            return Box(self.size + other)
        elif type(other) is Box:
            return Box(self.size + other.size)


    __radd__ = __add__        # 3 + a

    def __str__(self):
        return "[{} size={} length={}]".format(self.__class__.__name__,
                                     self.size, self.length)

if __name__ == '__main__':
    b1 = Box(10)
    b2 = Box(12)
    b3 = 3 + b1
    print b3 == Box(13)
    print b3 * 3