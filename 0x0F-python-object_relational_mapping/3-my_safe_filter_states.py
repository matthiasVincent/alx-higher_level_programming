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
    c = "SELECT * FROM states WHERE name = %s"
    cursor.execute(c, (state_name,))
    for d in cursor.fetchall():
        print(d)
    db.close()


if __name__ == '__main__':
    main()
