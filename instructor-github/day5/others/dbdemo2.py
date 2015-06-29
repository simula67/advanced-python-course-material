__author__ = 'ravi'

import MySQLdb
query = 'select version()'

with MySQLdb.connect('localhost', 'root', 'password', 'june12') as cur:
    cur.execute(query)
    print cur.description[0][0]
    print "^" * 12
    print cur.fetchone()[0]

