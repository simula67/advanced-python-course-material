__author__ = 'ravi'
import fileinput

for line in fileinput.input():
    print line.upper(),
