__author__ = 'ravi'

l = [2,3,4,1,6]

temp = []
for i in l:
    temp.append(i ** i)

print temp

#list comp
temp2 = [i**i for i in l]
print temp2

print [bin(i) for i in range(1, 6)]
