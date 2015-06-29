__author__ = 'antonjoj'

from sys import argv, stderr

if(len(argv) != 3):
    print >>stderr, "Usage: {} <source file> <destination file>".format(argv[0])
    exit(1)

lines = []
with open( argv[1]) as inp_file:
    for line in inp_file:
        lines.append(line)

lines.reverse()
with open(argv[2], "w") as out_file:
    for line in lines:
        print line
        out_file.write(line)