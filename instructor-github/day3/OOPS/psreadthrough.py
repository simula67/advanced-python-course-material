__author__ = 'ravi'
from pickle import load
from sys import argv
from pprint import  pprint

content = load(open(argv[1]))
print content[0]