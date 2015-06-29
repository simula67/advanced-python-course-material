__author__ = 'antonjoj'
import MySQLdb

conn = MySQLdb.connect('localhost','root', 'admin', 'june26')
query = "select version()"
cursor = conn.cursor()
cursor.execute(query)
print cursor.fetchall()
cursor.close()
conn.close()
