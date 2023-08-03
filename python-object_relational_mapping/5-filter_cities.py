#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()
    query = "SELECT cities.name \
            FROM cities \
            JOIN states \
                ON cities.state_id=states.id \
            WHERE states.name=%s \
            ORDER BY cities.id"

    state_name = sys.argv[4]
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    city_name = ", ".join(row[0] for row in rows)
    print(city_name)

    cursor.close()
    db.close()
