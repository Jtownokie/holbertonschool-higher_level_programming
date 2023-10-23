#!/usr/bin/python3
""" Contains MySQLdb script that queries a table """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' "\
            "ORDER BY id ASC".format(sys.argv[4])

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        if state[1] == sys.argv[4]:
            print(state)

    cursor.close()
    db.close()
