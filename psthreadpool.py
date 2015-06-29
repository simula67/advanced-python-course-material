__author__ = 'antonjoj'

import logging
import threading
from time import sleep

fmt="%(threadName)s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)


class ActivePool(object):

    def __init__(self):
        self.pool = []
        self.lock = threading.Lock()

    def make_active(self,name):
        with self.lock:
            self.pool.append(name)
            logging.debug('joined the pool :{}'.format(self.pool))

    def make_inactive(self,name):
        with self.lock:
            logging.debug('leaving pool')
            self.pool.remove(name)
            logging.debug('active pool {}'.format(self.pool))


def worker(sem, pool):
    logging.debug('waiting to join pool')
    name = threading.currentThread().name
    with sem:
        pool.make_active(name)
        sleep(5)
        pool.make_inactive(name)

if __name__ == '__main__':
    sem = threading.Semaphore(2)
    pool = ActivePool()
    for i in xrange(7):
        t = threading.Thread(target=worker, args=(sem, pool))
        t.start()