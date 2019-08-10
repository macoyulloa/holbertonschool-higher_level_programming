#!/usr/bin/python3
'list all states with a name starting with N'
from sys import argv
import MySQLdb
if __name__ == '__main__':
    'list all cities'
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                FROM cities INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY\
                cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    list_cities = []
    for row in query_rows:
        list_cities.append(row[0])
    print(", ".join(list_cities))
    cur.close()
    conn.close()
