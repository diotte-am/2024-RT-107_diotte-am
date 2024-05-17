"""
Amare Diotte
Data Engineering
GLAB 342.
"""

import mysql.connector as dbconnect
from mysql.connector import Error
import my_secrets

# a function that generates a user table and inserts it into the newly created database
def generate_user_table(conn):
    cursor = conn.cursor()
    # clear any existing table
    sql = ["DROP TABLE IF EXISTS user", 
           "CREATE TABLE `user`\
            (`email` varchar(100) NOT NULL,\
                `name` varchar(50) NOT NULL,\
                    `password` varchar(30))",
            """INSERT INTO user (email, name, password) VALUES\
                ('ywbaek@perscholas.edu', 'young', 'letsgomets'),\
                    ('mcordon@perscholas.org', 'marcial', 'perscholas'),\
                        ('mhaseeb@perscholas.org', 'haseeb', 'platform')""" ]
    for command in sql:
        cursor.execute(command)
    conn.commit()
    cursor.close()

# a function that takes name (string) and prints the corresponding email and password to the terminal
def get_user_by_name(conn, name):
    cursor = conn.cursor()
    cursor.execute("use RegistrationDB")
    cursor.execute("SELECT * FROM user where name = %s", (name,))
    records = cursor.fetchall()
    for record in records:
        print("Email: " + record[0] + "\nName: " + record[1] + "\nPassword: " + record[2] + "\n")
    
# takes the name of use and password, returns true if the individual is in the database, returns false otherwise
def validate_user(conn, email, password):
    cursor = conn.cursor()
    cursor.execute("use RegistrationDB")
    cursor.execute("SELECT email FROM user WHERE email = %s AND password = %s", (email, password))
    result = cursor.fetchall()
    print(len(result) > 0)

# takes the name of user and then the new values for name and password, prints True if rows are sucessfully updated, False if not
def update_user(conn, email, name, password):
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET name = %s, password = %s WHERE email = %s", (name, password, email))
    conn.commit()
    print(cursor.rowcount, "records affected")
    return cursor.rowcount > 0


# function connects to db and then calls all methods
def initialize():
    try:
        conn = dbconnect.connect(host='localhost', user=my_secrets.username, password=my_secrets.password)        
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS RegistrationDB")
        cursor.execute("use RegistrationDB")
        generate_user_table(conn)
        get_user_by_name(conn, "young")
        validate_user(conn, 'mcordon@perscholas.org', 'perscholas')
        validate_user(conn, 'root@perscholas.org', 'password')
        print("")
        print(update_user(conn, "mcordon@perscholas.org", "George", "Password"))
        print(update_user(conn, "mcordon@perscholas.com", "George", "Password"))







        if conn is not None and conn.is_connected():
            # Close connection
            cursor.close()
            conn.close()
    except:
        print("whoppes")






if __name__ == '__main__':
    initialize()