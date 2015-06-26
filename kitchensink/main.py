#!/usr/env python

# import Database class from Databases/mysql.py file
from Databases.mysql import Database

if __name__ == '__main__':
    db = Database()
    q = "DELETE FROM testTable"
    db.query(q)

    q = """
    INSERT INTO testTable
    (`name`, `age`)
    VALUES
    ('Mike', 39),
    ('Michael', 21),
    ('Angela', 21)
    """

    db.query(q)

    # Starting with 1.2.0, MySQLdb disables autocommit by default,
    # as required by the DB-API standard (PEP-249).
    # If you are using InnoDB tables or some other type of transactional table type,
    # you'll need to do connection.commit() before closing the connection,
    # or else none of your changes will be written to the database.

    db.connection.commit()

    q = """
    SELECT * FROM testTable
    WHERE age = 21
    """

    people = db.query(q)

    for person in people:
        print "Found: %s " % person['name']
