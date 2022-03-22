import mysql.connector

USERNAME = "altaf"
PASSWORD = "toor"

query = """
create database lyxelnflamingo;
create table lyxelnflamingo.resource (timestamp date, value int);
"""
try:
    connection = mysql.connector.connect( host ="localhost", user = USERNAME, password = PASSWORD )
    cursor = connection.cursor()
    cursor.execute(query)
finally:
    connection.close()
