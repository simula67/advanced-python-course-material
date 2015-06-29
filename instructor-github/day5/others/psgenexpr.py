__author__ = 'ravi'
import re

def grep_me(file, pattern):
    return (line for line in open(file) if re.search(pattern,line, re.I))

print grep_me('/etc/passwd', 'root')

for content in grep_me('/etc/passwd', 'root'):
    print content.rstrip()

