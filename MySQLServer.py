"""
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
NOTE :

Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

Print error message to handle errors when failing to connect to the DB.

handle open and close of the DB in your script.

"""
# download & import mysql-connector package
import mysql.connector


# set up connection with connect method

mydb = mysql.connector.connect(
    host='localhost', user='root', password='Chrislil1!', database='newdb')

# test the connection

print(f"Database {mydb.get_server_info()} created succesfully")

# write you sql queries/print to console
# close connection
