import mysql.connector
from mysql.connector import Error
import pandas as pd

#This program is for performing queries on the local MySQL server

#mysql password
#IMPORTANT: DELETE THIS BEFORE GIT COMMIT
pw = 'ABCDEFG'

#re-usable connect to mySQL server function
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#re-usable create database function
#note: only run this once for this project
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Database Created Successfully')
    except Error as err:
        print(f"Error: '{err}'")
        
#re-usable connect to database function
def create_database_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection succesful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#re-usable function to execute any SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")

#SCRIPTING & QUERIES
connection = create_database_connection("localhost", "root", pw, "bjj")
