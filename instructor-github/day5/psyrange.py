__author__ = 'ravi'

class yrange(object):
    def __init__(self, stop_value):
        self.start_value = 0
        self.stop_value = stop_value

    def __iter__(self):
        while True:
            yield self.start_value
            self.start_value += 1

            if self.start_value == self.stop_value:
                raise StopIteration()

if __name__ == '__main__':
    for i in yrange(5):
        print i

