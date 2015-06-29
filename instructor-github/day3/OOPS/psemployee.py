__author__ = 'ravi'
from psperson import Person

class Employee(Person):
    def __init__(self, eid, first_name, last_name,
                 gender, designation):
        self.eid = eid

        self.designation = designation
        """call base class version of __init__"""

        super(Employee, self).__init__(first_name, last_name, gender)
        self.age = None

    def get_info(self):

        print "employee id : {}".format(self.eid)
        super(Employee, self).get_info()
        print "designation : {}".format(self.designation)
        print "age : {}".format(self.age)


if __name__ == '__main__':
    e = Employee('v4001', 'guido', 'rossum', 'male', 'clerk')
    print dir(e)
    #Person.get_info(e)
    e.get_info()
