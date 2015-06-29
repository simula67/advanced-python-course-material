__author__ = 'ravi'

l = [5, 'pam', 4, 'anderson', 1, 3]
l[-3] = 'pam pam'

print l[-1]
print l[-2]
print l

sort_form_l = sorted(l, reverse=True)

"""
#l.sort(reverse=True)

for i in sorted(l, reverse=True):
    print i

print l
"""