"""
string format ( old style )
"""

from math import pi
r = 2.2
area = pi * r * r
print "Radius : %f \nArea : %.3f" % (r , area)


"""
string format ( new style )
{index:fmt}
"""
print "Radius : {} \nArea : {:.3f}".format(r , area)
