#!/usr/bin/python3
"""
Script that displays all values in the states table where
name matches the argument (safe from SQL injection).
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * \
                   FROM states \
                   WHERE name = %s \
                   ORDER BY id"
    state_name = (sys.argv[4],)
    cursor.execute(query, state_name)

    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
