#!/usr/bin/python3
"""
Displays all values in the state where name matches the argument
"""

import MySQLdb
from sys

if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    states = db_cursor.fetchall()

    for state in states:
        print(state)
