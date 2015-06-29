__author__ = 'ravi'

i = 1

while i <= 5:
    if i == 4:
        break
    elif i == 1:
        print 'i'
    elif i == 2:
        print "two"
    elif i == 3:
        i += 1
        continue
    else:
        print i
    i += 1
else:
    print "else block to the while loop"
