__author__ = 'ravi'
from sys import argv

def get_file_objects():
    for file_name in argv[1:]:
        yield open(file_name)

def input():
    for fo in get_file_objects():
        for line in fo:
            yield line

for ln in input():
    print ln,
