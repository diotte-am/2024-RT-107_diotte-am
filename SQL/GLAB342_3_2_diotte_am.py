"""
Amare Diotte
Data Engineering
GLAB 342.3.2 Insert Data into MySQL from Python
"""

import mysql.connector as dbconnection
from mysql.connector import Error
import my_secrets

# creating a table - this assumes a database named registrationDB already exists
try:
    conn = dbconnection.connect(database = 'registrationDB', user = my_secrets.username, password = my_secrets.password, host = "localhost" )
    cursor = conn.cursor()
    sql = "CREATE TABLE `laptop` (`id` int(11) NOT NULL,\
        `Name` varchar(250) NOT NULL,\
            `Price` float NOT NULL,\
                `Purchase_date` date NOT NULL)"
    cursor.execute(sql)
    print("Table is created")
except Error as e:
    print("Falied to create table {}".format(e))
finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")

# insert a single row into mysql table from python
try:
    conn = dbconnection.connect(database = 'registrationDB', user = my_secrets.username, password = my_secrets.password, host = "localhost" )
    cursor = conn.cursor()
    sql_insert = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)\
    VALUES (15, 'Lenovo ThinkPad P71', 6459, '2019-08-15')"""
    cursor.execute(sql_insert)
    # commit needed to update DB
    conn.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()
except Error as e:
    print("Failed to insert record into Laptop table {}".format(e))
finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")

# Use Python Variables
def insert_tables(id, name, price, purchase_date):
    try:
        conn = dbconnection.connect(database = 'registrationDB', user = my_secrets.username, password = my_secrets.password, host = "localhost" )
        cursor = conn.cursor()
        sql_insert = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)\
        VALUES (%s, %s, %s, %s)"""
        # put one row of parameters in one tuple
        record = (id, name, price, purchase_date)
        cursor.execute(sql_insert, record)
        conn.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        cursor.close()
    except Error as e:
        print("Failed to insert record into Laptop table {}".format(e))
    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed")

# Insert Multiple rows into a databaase
def insert_multiple():
    try:
        conn = dbconnection.connect(database = 'registrationDB', user = my_secrets.username, password = my_secrets.password, host = "localhost" )
        cursor = conn.cursor()
        # string where values will be inserted
        sql_insert = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)\
        VALUES (%s, %s, %s, %s)"""
        # 4 rows to insert
        record = [(4, 'HP Pavilion Power', 1999, '2019-01-11'), (5, 'MSI WS75 9TL-496', 5799, '2019-07-23'), (6, 'Microsoft Surface', 2330, '2019-07-23')]
        # execute all records
        cursor.executemany(sql_insert, record)
        conn.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")
        cursor.close()
    except Error as e:
        print("Failed to insert record into Laptop table {}".format(e))
    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection is closed")

insert_tables(2, "Area 51M", 6999, '2019-04-14')
insert_tables(3, 'MacBook Pro', 2499, '2019-06-20')
insert_multiple()

