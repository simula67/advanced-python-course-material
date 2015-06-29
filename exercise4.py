__author__ = 'antonjoj'

ul = [l.rstrip().split(':') for l in open("datafiles\\passwd")]
print sorted(ul, key=lambda elem: int(elem[2]))