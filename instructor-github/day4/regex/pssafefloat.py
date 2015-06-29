__author__ = 'ravi'
from sys import argv, exc_info

def safe_float(value):
    try:
        temp = None
        temp = float(value[1]) / 0
    except ValueError, e:
        print e
    except TypeError, e:
        print "handling type error", e
    except (IndexError, KeyError), e:
        print e
    except:
        print exc_info()[1]
        print "internal server error"
    finally:
        print "finally block of the try"
        return temp


if __name__ == '__main__':
    print safe_float(argv)
