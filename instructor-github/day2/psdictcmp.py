__author__ = 'ravi'
from pprint import pprint
"""
u = {l.split(':')[0]: l.rstrip().split(':')[1:]
            for l in open('/etc/passwd')}
"""
users = {}

for line in open('/etc/passwd'):
    temp = line.rstrip().split(':')
    users[temp[0]] = temp[1:]

for login in sorted(users):
    print "{}:{}".format(login, users[login][-1])