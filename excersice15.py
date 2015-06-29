__author__ = 'antonjoj'

# Implement >> and << to get n lines
# Also implement file equality

from hashlib import md5
from collections import deque

class CustomFile(file):

    def __eq__(self, other):
        return md5(self.read()).hexdigest() == md5(other.read()).hexdigest()


    def __rshift__(self, other):
        result = []
        for line in self:
            result.append(line)
            other -= 1
            if other <= 0:
                return result

    def __lshift__(self, other):
        return list(deque(self, other))

fp1 = CustomFile("datafiles\\passwd")
print fp1 >> 5
print fp1 << 5

fp2 = CustomFile("datafiles\\passwd")
fp3 = CustomFile("datafiles\\passwd")
print fp2 == fp3
