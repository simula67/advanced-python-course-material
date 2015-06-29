__author__ = 'ravi'
from pprint import pprint
from collections import  deque
from hashlib import md5

class CustomFile(file):
    def __eq__(self, other):
        return \
            md5(self.read()).hexdigest() == \
            md5(other.read()).hexdigest()

    def __lshift__(self, other):
        temp = []
        count = 1
        while count <= other:
            temp.append(self.readline())
            count += 1
        return temp

    def __rshift__(self, other):
        return list(deque(self, other))

if __name__ == '__main__':
    with CustomFile('/etc/passwd') as fp:
        pprint(fp << 2)
        print
        pprint(fp >> 2.5)

    with CustomFile('/etc/passwd') as f1,\
                CustomFile('/etc/passwd') as f2:
        print f1 == f2

