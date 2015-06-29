__author__ = 'ravi'
from pprint import pprint

import MySQLdb
query = 'select version()'

content = [(record[0], record[4], record[-1]) for record in
            (line.rstrip().split(':') for line in open('/etc/passwd'))]

query = r"insert into passwd (name, gecos, shell) values (%s, %s, %s)"
#pprint(content); exit(1)

with MySQLdb.connect('localhost', 'root', 'password', 'june12') as cur:
    #help(cur.executemany)
    cur.executemany(query, content)



