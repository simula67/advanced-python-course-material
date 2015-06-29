"""
a sample python module
"""
from os import getpid, listdir
import sys

__all__ = ['pid', 'Dummy', 'name']

name = "hp"
city = 'bangalore'
version = 0.1


def pid():
    """
    pid(), gets you the current process id
    :return:
    """
    print "process id : {}".format(getpid())


def ls(path="."):
    """
    ls(), list the content of the given directory
    :param path: directory path
    :return:
    """
    for file_name in listdir(path):
        print file_name


class Dummy(object):
    """
    Dummy, a dummy class for the python module
    """
    def get_item(self):
        """
        return an item of a current object
        :return:
        """
        return "a dummy note"


def main():
    print __name__
    print Dummy
    d = Dummy()
    print d.get_item()
    pid()
    print name

if __name__ == '__main__':
    main()