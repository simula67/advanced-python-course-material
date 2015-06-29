__author__ = 'antonjoj'

class yrangeIterator(object):
    def __init__(self, o_yrage):
        self.yr = o_yrage


    def __iter__(self):
        pass

    def next(self):
        self.yr.start_value += 1
        if self.yr.start_value <= self.yr.stop_value:
            return self.yr.start_value - 1
        else:
            raise StopIteration


class yrange(object):


    def __init__(self, stop_value):
        self.start_value = 0
        self.stop_value = stop_value

    def __iter__(self):
        return yrangeIterator(self)

if __name__ == '__main__':
    print iter(yrange(5))
    for i in yrange(5):
        print i