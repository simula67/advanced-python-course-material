__author__ = 'antonjoj'

class ConnectionPool(object):
    max_connection = 5;
    conn_counter = 0

    def __init__(self, cid):
        ConnectionPool.check_count()
        self.cid = cid
        ConnectionPool.conn_counter += 1

    def check_count():
        if ConnectionPool.conn_counter > ConnectionPool.max_connection:
            raise RuntimeError("reached maximum allowable connections")

    print check_count
    # Following line does the same thing as using @statidmethod decorator on check_count
    check_count = staticmethod(check_count)
    print check_count

if __name__ == '__main__':
    try:
        for i in range(1,10):
            ConnectionPool("c" + str(i))
    except RuntimeError, e:
        print e
    finally:
        print "done"