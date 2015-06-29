__author__ = 'antonjoj'

from sys import stderr
from sys import argv


def usage():
    print >> stderr, "{} <source1> [source2] ... <target>".format(argv[0])
    exit(1)

def copy_all(*args):
    if(len(args) < 2):
        usage()
    target = args[-1]
    print "Target is {}".format(target)
    with open(target, "w") as target_fp:
        for i in range(0, len(args) -1):
                target_fp.write(args[i].center(15,'-') + "\n")
                with open(args[i]) as fp:
                    for line in fp:
                        print line,
                        target_fp.write(line)
                target_fp.write("\n" + "".center(15,'-') + "\n")

print argv
copy_all(*argv[1:])