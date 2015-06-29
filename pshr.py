__author__ = 'antonjoj'

class Person(object):
    def __init__(self, fname, lname, gender):
        self.first_name = fname
        self.last_name = lname
        self.gender = gender

    def get_info(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.gender)


class Employee(Person):

    def __init__(self, fname, lname, gender, eid, designation):
        super(Employee, self).__init__(fname, lname, gender)
        self.eid = eid
        self.designation = designation

    def get_info(self):
        return super(Employee, self).get_info() + " {} {}".format(self.eid, self.designation)


john = Employee("John", "Olliver", "Male", 12, "Comedian")
print john.get_info()
