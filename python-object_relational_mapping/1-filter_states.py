#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve states with names starting with N
    cursor.execute("SELECT * \
                   FROM states \
                   WHERE name LIKE BINARY 'N%' \
                   ORDER BY id")

    # Fetch all the rows and display them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection to the database
    cursor.close()
    db.close()
