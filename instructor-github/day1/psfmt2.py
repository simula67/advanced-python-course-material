from math import pi

r = 2.2 
area = pi * (r ** 2)
"""
{index:fmt}
"""

s =  "Radius : {0}\nArea : {1:.3f}".format(r, area) 
print s.upper()

