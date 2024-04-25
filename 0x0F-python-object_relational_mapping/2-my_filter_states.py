#!/usr/bin/python3

import MySQLdb
import sys

def FilSt():
    args = sys.argv
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user = args[1],
        password = args[2],
        database= args[3],
        charset="utf8"
    )
    mycursos= mydb.cursor()
    mycursos.execute("""SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC""".format(args[4]))

    result = mycursos.fetchall()
    for raw in result:
        print(raw)
        
if __name__ == "__main__":
    FilSt()
