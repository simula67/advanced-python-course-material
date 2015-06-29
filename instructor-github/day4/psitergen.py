__author__ = 'ravi'
import  re

class MatchIt(object):
    def __init__(self, file_name, pattern):
        self.fp = open(file_name)
        self.pattern = pattern


    def nt(self):
            for content in self.fp:
                if not content:
                    raise StopIteration
                if re.search(self.pattern, content):
                    yield content

if __name__ == '__main__':
    g = MatchIt('/etc/passwd', 'root').nt()
    print g
    for i in g:
        print i,