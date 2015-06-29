__author__ = 'antonjoj'

import threading
from time import sleep
import logging

fmt =  "%(threadName)s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)

def worker(delay, lock):
    sleep(delay)
    logging.debug("Waiting for lock")
    with lock:
        logging.debug("Acquired lock")
        print "child : {}".format(threading.currentThread().ident)
        logging.debug("Released lock")

if __name__ == '__main__':
    lock = threading.Lock()
    for i in xrange(10):
        t = threading.Thread(target=worker, args=(2,lock))
        t.start()
    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()

    print "end of main thread"