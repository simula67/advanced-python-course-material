__author__ = 'ravi'
# http://www.codegood.com/archives/tag/mysqldb
import MySQLdb
conn = MySQLdb.connect('localhost', 'root', 'password', 'may22')
cur = conn.cursor()

query = """
create table lang(
    id int primary key auto_increment,
    lang varchar(32),
    version varchar(12)
)
"""

#cur.execute(query)
cur
cur.close()
conn.close()
