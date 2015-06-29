"""
a sample python module
"""

from os import getpid, listdir

name = "hp"
city = "bangalore"
version = "0.0.1"

def pid():
    """
    pid(), gets you the current process id
    :return:
    """
    print "procss id = {}".format(getpid())

def ls(path="."):
    """
    ls() list the content of the given directory
    :param path: directory path
    :param path:
    :return:
    """
    for file_name in listdir(path):
        print file_name

class Dummy(object):
    """
    Dummy class for the python module
    """

    def get_item(self):
        """
        return an item of the curent object
        :return:
        """
        return "a dummy note"


def main():
    print __name__
    d = Dummy()
    print d.get_item()
    pid()
    print name


main()