import bz2

import sys
import os

bz = bz2.BZ2File('testit_bz2', 'w')

fp = open('/etc/passwd')

bz.write(fp.read())

fp.close()
bz.close()
