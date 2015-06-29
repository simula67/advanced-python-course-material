__author__ = 'antonjoj'

class RangeError(Exception):

    def __init__(self, message, remedy):
        super(RangeError, self).__init__(message)
        self.remedy = remedy

    def __str__(self):
        return "{} : {} {}".format(self.__class__.__name__, self.message , self.remedy)

def check_radition(limit):
    if limit > 7:
        raise RangeError("Range is too high : {}, ".format(limit), "value should be less than 7")

try:
    check_radition(2100)
except RangeError, e:
    print e