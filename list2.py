__author__ = 'antonjoj'

l1 = [1,2,3]
l2 = range(4,11)
l3 = range(11, 16)

l1.extend(l2)
print l1

print l1 + l3
print l1
l1.reverse() # inplace reverse !!!
print l1
print l1[::-1] ## non - inplace reverse !!!


l4  = [ 5,4,"anderson", 3.2,1,9]
l4.sort()
print l4 # Again inplace !!!

l4.sort(reverse=True)
print l4

l4.sort()

for i  in sorted(l4, reverse=True):
    print i

# See the above code did not change the list
print l4