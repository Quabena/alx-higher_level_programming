#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials, database name, and state name from arguments
    username, password, db_name, state_name = sys.argv[1], sys.argv[2],
    sys.argv[3], sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to find states matching the argument
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;"
    .format(state_name)
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state in the desired format
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()