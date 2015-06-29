import logging
import threading
from time import sleep

fmt = "%(threadName)s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)


class ActivePool(object):
    def __init__(self):
        self.pool = []
        self.lock = threading.Lock()

    def make_active(self, name):
        with self.lock:
            self.pool.append(name)
            logging.debug('joined the pool: {}'.format(self.pool))

    def make_inactive(self, name):
        with self.lock:
            logging.debug("leaving the pool")
            self.pool.remove(name)
            logging.debug('active pool: {}'.format(self.pool))


def worker(sem, pool):
    name = threading.currentThread().name
    logging.debug('waiting to join the pool')
    with sem:
        pool.make_active(name)
        sleep(3)
        pool.make_inactive(name)

if __name__ == '__main__':
    s = threading.Semaphore(3)
    p = ActivePool()
    for i in xrange(7):
        t = threading.Thread(target=worker, args=(s, p))
        t.start()

for t in threading.enumerate():
    if t is not threading.currentThread():
        t.join()
