__author__ = 'ravi'

s = 'pypi'

for item in s:
    if item not in 'aeiou':
        for i in range(1, 3):
            print item * i

