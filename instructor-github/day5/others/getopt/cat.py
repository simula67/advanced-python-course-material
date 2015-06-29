#!/usr/bin/env python
import getopt
import sys
def usage():
    print "Usage : %s  -r filename "  % sys.argv[0]
    exit(1) 

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "-f:rh")
    except getopt.GetoptError as err:
        usage()
    reverse = False
    print opts
    for item in opts:
	if '-r' in item:
		reverse = True
    content = open(args[0]).readlines()
    if reverse:
	print ''.join(content[::-1])
    else:
        print ''.join(content)

if __name__ == "__main__":
    main()
