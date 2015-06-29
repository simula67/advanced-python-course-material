__author__ = 'ravi'

import MySQLdb

conn = MySQLdb.connect('localhost', 'root', 'password', 'june12')

query = 'select version()'

cur = conn.cursor()
cur.execute(query)
print cur.description[0][0]
print "^" * 12
print cur.fetchone()[0]

cur.close()
conn.close()
