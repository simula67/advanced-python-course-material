__author__ = 'ravi'

with open('/etc/passwd') as fp:
    #for line in fp:
    line = ''
    line += fp.readline()
    line += fp.readline()
    for line in range(10):
        print str(line) + "\n",



