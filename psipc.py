__author__ = 'antonjoj'


import multiprocessing
import subprocess
from os import getpid
from time import sleep

def task( rd, wt):
    cmd = rd.recv()
    output = subprocess.check_output(cmd, shell=True)
    wt.send(output)


if __name__ == '__main__':
    r1, w1 = multiprocessing.Pipe()
    r2, w2 = multiprocessing.Pipe()
    child = multiprocessing.Process(target=task, args=(r1,w2))
    child.start()
    w1.send("dir")
    print r2.recv()
