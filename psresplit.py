__author__ = 'antonjoj'
import re

s= "root,x:0;0 administrator"
print re.split(r'[\ ,:;]' ,s)