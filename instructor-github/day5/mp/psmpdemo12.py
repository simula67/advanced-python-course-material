__author__ = 'ravi'
import multiprocessing
from os import getpid
from time import sleep

def task_set(delay):
    print "child process id : {}".format(getpid())
    sleep(delay)

def main():
    print "parent process id : {}".format(getpid())
    for _ in xrange(5):
        p = multiprocessing.Process(target=task_set, args=(2, ))
        p.start()

    for child in multiprocessing.active_children():
        child.join()
    print "parent process end here"

if __name__ == '__main__':
    main()

