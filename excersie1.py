__author__ = 'antonjoj'

# Take as input electricity consumed and print and billable amount

consumed = int(raw_input("How many units of electricy was consumed ? : "))
billable = 0

if consumed <= 100:
    billable = consumed
elif consumed > 100 and consumed <= 200:
    billable = consumed * 1.5
elif consumed > 200 and consumed <= 500:
    billable = 400 + ( consumed - 200 ) * 3
else:
    billable = 1800 + ((consumed - 500) * 5.75 )

print "Billable amount is : {}".format(billable)