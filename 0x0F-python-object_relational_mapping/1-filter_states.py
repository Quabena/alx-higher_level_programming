#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state in the desired format
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
