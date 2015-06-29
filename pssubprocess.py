__author__ = 'antonjoj'

import subprocess

print "Python 2.7 version START".center(30, "-")
op1 = subprocess.check_output("dir", shell=True)
print op1
print "Python 2.7 version END".center(30, "-")

print "Python 2.6 version START".center(30, "-")

op2 = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE)
for line in op2.communicate():
    if line:
        print line

print "Python 2.6 version END".center(30, "-")