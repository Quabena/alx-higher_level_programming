#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ = "__main__":
    # Get MySQL credentials and database from the arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor to execute the SQL queries
    cursor = db.cursor()

    # Execute the query to retrieve states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"

    # Fetch the results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor
    cursor.close()

    # Close the connection
    db.close()
