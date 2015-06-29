name = "pam"
gender = "female"
age = 2

print "|{}|{}|{}|".format(name,gender,age) # no colum width
print "|{:>12}|{:>12}|{:>5}|".format(name,gender,age) # colum width + right aligned
print "|{:<12}|{:<12}|{:<5}|".format(name,gender,age) # colum width + left aligned
print "|{:^12}|{:^12}|{:^5}|".format(name,gender,age) # colum width + center aligned
print "|{:12}|{:12}|{:5}|".format(name,gender,age) # colum width + default aligned
