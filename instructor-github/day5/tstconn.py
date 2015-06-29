__author__ = 'ravi'
import MySQLdb

conn = MySQLdb.connect('localhost', 'root', '', 'june26')
query = "select version()"
cur = conn.cursor()
cur.execute(query)

print cur.fetchall()

cur.close()
conn.close()
