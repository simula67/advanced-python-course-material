__author__ = 'antonjoj'

from os import getpid
from time import sleep
import multiprocessing

def task():
    sleep(1)
    print "Child pid {}".format(getpid())

if __name__ == '__main__':
    for _ in range(10):
        p = multiprocessing.Process(target=task)
        p.start()
    for child in multiprocessing.active_children():
        child.join()
    print "Main process exiting"
