import MySQLdb
query = 'select id, name, shell from passwd limit 10'

with MySQLdb.connect('localhost', 'root', 'password', 'june12') as cur:

    cur.execute('delete from passwd where id = 1')

    cur.execute(query)
    print "{:>6} {:>18} {:>18}".format(cur.description[0][0],
                                       cur.description[1][0],
                                       cur.description[2][0],
                                       )
    for row in cur.fetchall():
        print "{:>6} {:>18} {:>18}".format(*row)

