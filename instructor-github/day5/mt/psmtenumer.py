__author__ = 'ravi'
import threading
from time import sleep
import logging
from random import randint

fmt= "%(threadName)s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)

def worker(delay, lock):
    logging.debug("waiting for the lock")
    with lock:
        logging.debug("acquired lock")
        print "child : {}".format(threading.currentThread().name)
        sleep(delay)
        logging.debug("releases the lock")

if __name__ == '__main__':
    lock = threading.Lock()
    for i in xrange(5):
        t = threading.Thread(target=worker, args=(2, lock))
        t.start()

    for t in threading.enumerate():
        if t is not threading.currentThread():
            t.join()

    print "end of the main thread"

