#!/usr/env python

# Install on Mac OS X
# 1) brew install python To install Python 2.7
# 2) brew install mysql To install mysql to the system (needed for various drivers)
# 3) Configured mysql per homebrew's recommendations
# 4) Downloaded mysql_python (http://sourceforge.net/projects/mysql-python/files/mysql-python/1.2.3/) and unzipped it
# 5) Installed mysql_python using python setup.py install
# 6) Tested it in an interactive session python, import _mysql

import MySQLdb

class Database:
    
    host = "127.0.0.1" #127.0.0.1 uses the socket, localhost uses TCP/IP
    user = "testuser"
    passwd = "testpass"
    db = "test"
    
    def __init__(self):
        self.connection = MySQLdb.connect(host=self.host, 
                                          user=self.user, 
                                          passwd=self.passwd, 
                                          db=self.db)
    def query(self, q):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q)
        return cursor.fetchall()
        
    def __del__(self):
        self.connection.close()
        
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
    