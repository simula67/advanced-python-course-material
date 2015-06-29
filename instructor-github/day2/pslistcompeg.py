__author__ = 'ravi'
from pprint import pprint
"""
ul = sorted([l.split(':')[0].title() for l in open('/etc/passwd')
                if l.startswith('a')])
"""

ul = [l.rstrip().split(':') for l in open('/etc/passwd')]

pprint(ul)