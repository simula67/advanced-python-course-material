__author__ = 'ravi'
import multiprocessing
import subprocess
from os import getpid
from time import sleep

def task_set(rd, wt):
    cmd = rd.recv()
    wt.send(subprocess.check_output(cmd, shell=True).upper())

def main():
    r1, w1 = multiprocessing.Pipe()  #parent to write
    r2, w2 = multiprocessing.Pipe()
    child = multiprocessing.Process(target=task_set, args=(r1, w2))
    child.start()
    w1.send('ls -l')
    print r2.recv()

if __name__ == '__main__':
    main()

