__author__ = 'antonjoj'

import re
class Mather(object):
    def __init__(self,filename,pattern):
        self.filename = filename
        self.pattern = pattern

    def __iter__(self):
        return self

    def next(self):
        with open(self.filename) as fp:
            content = fp.readline()
            if not content:
                raise StopIteration
            if re.search(self.pattern, content):
                yield content

mather = Mather("datafiles\\passwd", "r")

for i in mather:
    print i

