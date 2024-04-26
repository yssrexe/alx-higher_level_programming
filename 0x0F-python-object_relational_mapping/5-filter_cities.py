#!/usr/bin/python3
"""
    a script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=args[1],
                         passwd=args[2],
                         db=args[3],
                         charset="utf8"
                         )
    cur = db.cursor()
    statement = """SELECT c.name
                    FROM cities AS c
                    JOIN states AS s
                    ON c.state_id = s.id
                    WHERE BINARY s.name = %s
                    ORDER BY c.id ASC
                """
    cur.execute(statement, (args[4],))

    query_rows = cur.fetchall()
    print(', '.join(tuple(row[0] for row in query_rows)))
