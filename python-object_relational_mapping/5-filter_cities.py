#!/usr/bin/python3
""" Contains MySQLdb script that queries a table """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    state_input = sys.argv[4]

    cursor.execute("""
        SELECT cities.name
        FROM cities JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_input, ))
    cities = cursor.fetchall()

    for row in cities:
        print(row)

    cursor.close()
    db.close()
