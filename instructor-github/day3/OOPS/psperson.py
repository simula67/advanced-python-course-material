__author__ = 'ravi'

class Person(object):
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = 0


    def get_info(self):
        print "first name : {}".format(self.first_name)
        print "last name : {}".format(self.last_name)
        print "gender : {}".format(self.gender)

if __name__ == '__main__':
    p = Person('larry', 'wall', 'male')
    p.get_info()

