#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor objet
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    cursor.execute('SELECT * FROM states ORDER BY id')

    # Fetch all the rows and display them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection to the database
    cursor.close()
    db.close()
