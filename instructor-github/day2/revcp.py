__author__ = 'ravi'
from sys import argv, stderr


def reverse_copy(source_file, dest_file):
    content = open(source_file).readlines()[::-1]
    open(dest_file, 'w').writelines(content)

def usage():
    print >>stderr, "Usage:"
    print >>stderr, "{} source-file dest-file".format(argv[0])
    exit(1)

if len(argv) != 3:
    usage()

try:
    reverse_copy(argv[1], argv[2])
except IOError, e:
    print e