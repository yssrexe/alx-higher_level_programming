#!/usr/bin/python3
"""print all states from hbtn_0e_0_usa database"""
import MySQLdb
import sys


def ShowAll():
    args = sys.argv
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        password=args[2],
        database=args[3],
        charset="utf8"
    )

    mycursor = mydb.cursor()
    mycursor.execute("""SELECT c.id, c.name, s.name
                    FROM cities AS c
                    JOIN states AS s
                    ON c.state_id = s.id
                    ORDER BY c.id ASC
                """)
    result = mycursor.fetchall()

    for row in result:
        print(row)


if __name__ == "__main__":
    ShowAll()
