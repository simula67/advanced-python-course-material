__author__ = 'ravi'
import threading
from time import sleep

def worker():
    sleep(2)
    print "child : {}".format(threading.currentThread().ident)


if __name__ == '__main__':
    threads = []
    for i in xrange(10):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  #main thread to wait for its child thread

    print "end of the main thread"

