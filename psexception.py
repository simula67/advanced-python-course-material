__author__ = 'antonjoj'

from sys import argv, exc_info

def safe_float(value):
    try:
        temp = None
        temp = float(value[1]) / float(value[2])
    # handle an exception
    except ValueError, e:
        print e
    # Handle one more
    except TypeError, e:
        print "Type error"
        print e
    # Hnadle more than on in a single block
    except (IndexError, KeyError), e:
        print e
    # Generic handler
    except:
        print exc_info()[1]
    finally:
        return temp

if __name__ == '__main__':
    print safe_float(argv)

