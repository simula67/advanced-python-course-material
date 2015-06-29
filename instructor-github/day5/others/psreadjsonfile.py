__author__ = 'ravi'
from json import load
from pprint import pprint

content = load(open('rootcap.json'))
for dir_name in  content[0]:
    print dir_name
