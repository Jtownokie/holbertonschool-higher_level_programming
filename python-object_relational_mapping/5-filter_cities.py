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
        SELECT name FROM cities
        WHERE state_id = 
            (SELECT id
            FROM states
            WHERE name = %s)
        ORDER BY cities.id ASC
    """, (state_input, ))
    cities = cursor.fetchall()

    print(cities)

    cursor.close()
    db.close()
