__author__ = 'ravi'

mat = [[1, 2, 3],
       [4, 5, 6, 10],
       [7, 8, 9]]

print [c for r in mat if len(r)==3 for c in r if c%2]

"""
for row in mat:
    for col in row:
        print "{}\t".format(col),
    print

print [row[1] for row in mat]
"""