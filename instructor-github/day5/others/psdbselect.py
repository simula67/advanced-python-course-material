__author__ = 'ravi'
# http://www.codegood.com/archives/tag/mysqldb
import MySQLdb
conn = MySQLdb.connect('localhost', 'root', 'password',
                       'may22', autocommit=True)
cur = conn.cursor()

query = 'select * from lang'
cur.execute(query)

for row in cur.fetchall():
    print "{:>6} {:>12} {:>12}".format(*row)

cur.close()
conn.close()
