#!/usr/bin/python3
'list all states with a name starting with N'
from sys import argv
import MySQLdb
if __name__ == '__main__':
    'list all states'
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\
            ORDER BY id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
