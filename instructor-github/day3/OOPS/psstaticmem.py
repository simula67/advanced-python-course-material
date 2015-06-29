__author__ = 'ravi'

class ConnectionPool(object):
    max_connection = 5
    conn_counter = 1

    def __init__(self, cid):
        self.check_count()
        self.cid = cid
        ConnectionPool.conn_counter += 1

    @staticmethod
    def check_count():
        if ConnectionPool.conn_counter > ConnectionPool.max_connection:
            raise RuntimeError("reached maximum allowable connection")

if __name__ == '__main__':
    try:
        c = []
        for cid in range(1, 10):
            c.append(ConnectionPool("c"+str(cid)))
    except RuntimeError, e:
        print e
    finally:
        for connection in c:
            print connection.cid
