__author__ = 'ravi'

class RangeError(Exception):
    def __init__(self, message, remedy):
        super(RangeError, self).__init__(message)
        self.remedy = remedy

    def __str__(self):
        return "{}: {}\n{}".format(self.__class__.__name__,
                               self.args[0], self.remedy)

def check_radiation(limit):
    if limit > .7:
        raise RangeError("its too high: {}".format(limit),
                         "permitted limit 0.3 <= radiation <= 0.6")

try:
    check_radiation(.9)
except RangeError, e:
    print e