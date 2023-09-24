#!/usr/bin/python3
"""
    Displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
"""


import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve states matching the provided name
    query = "SELECT * FROM states WHERE name=%s ORDER BY id"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
