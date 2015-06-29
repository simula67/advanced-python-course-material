__author__ = 'ravi'

name = ['pam', 'aman', 'mike', 'kim']
gender = ['female', 'male', 'female', 'female']
age = [2, 4, 4, 1]

lt = zip(name, gender, age)
print lt

def sort_it(record, other):
    if cmp(record[-1], other[-1]) == 0:
        return cmp(record[1], other[1])
    else:
        return cmp(record[-1], other[-1])

lt.sort(cmp=sort_it)

print lt

"""
lt.sort(key=lambda record: record[-1])
print lt
"""
