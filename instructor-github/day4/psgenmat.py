__author__ = 'ravi'
import re

class DemoGen(object):
    def grepit(self, file_name, pattern):
        for line in open(file_name):
            if re.search(pattern, line):
                yield line

#print grepit('/etc/passwd', 'root'); exit(1)

for line in DemoGen().grepit('/etc/passwd', 'root'):
    print line,