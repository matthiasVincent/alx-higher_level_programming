#!/usr/bin/python3
"""
This file prints all states from the database
"""

import sys
import MySQLdb


def main():
    """
    This file use a mysql search from python
    """
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_password, db=db_name)
    cursor = db.cursor()
    sqlquery = "SELECT cities.name FROM cities JOIN states ON\
            states.id = cities.state_id\
            WHERE states.name = %s ORDER BY cities.id"
    cursor.execute(sqlquery, (state_name,))
    data = cursor.fetchall()

    for i in range(len(data)):
        if (i != len(data) - 1):
            print(data[i][0] + ", ", end="")
        else:
            print(data[i][0], end="")
    print()
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
