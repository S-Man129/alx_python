#!/usr/bin/python3
"""
    lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", 
                         port=3306, 
                         user=username, 
                         passwd=password, 
                         db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
