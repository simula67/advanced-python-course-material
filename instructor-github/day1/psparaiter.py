__author__ = 'ravi'

name = ['pam', 'aman', 'mike', 'kim']
gender = ['female', 'male', 'female', 'female']
age = [2, 4, 4, 1]

lt = zip(name, gender, age)
print lt

lt.sort(key=lambda record: record[-1])
print lt

