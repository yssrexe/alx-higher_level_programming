#!/usr/bin/python3
import MySQLdb
import sys
"""
   a script that takes in an argument and displays all values
"""


if __name__ == "__main__":
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
    stat = """SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"""
    mycursor.execute(stat, (args[4],))
    result = mycursor.fetchall()
    for row in result:
        print(row)
