__author__ = 'ravi'
# http://www.codegood.com/archives/tag/mysqldb

import MySQLdb
conn = MySQLdb.connect('localhost', 'root', 'password', 'may22')

cur = conn.cursor()

cur.execute('select version()')


row = cur.fetchone()

print cur.description[0][0]
print '-' * 10
print row[0]

cur.close()
conn.close()
