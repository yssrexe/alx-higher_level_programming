#!/usr/bin/python3
"""print all states from hbtn_0e_0_usa database"""
import MySQLdb
import sys

def ListAllSt():
    args = sys.argv
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user= args[1],
        password= args[2],
        database = args[3],
        charset="utf8"
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    result = mycursor.fetchall()
    for row in result:
        print(row)
        

if __name__ == "__main__":
    ListAllSt()
