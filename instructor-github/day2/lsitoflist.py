__author__ = 'ravi'

ul = [l.rstrip().split(':') for l in open('/etc/passwd')]

for user in sorted(ul, key=lambda users: int(users[2])):
    print "{}:{}:{}".format(user[2], user[0], user[-1])
