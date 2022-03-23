import json
import falcon
import mysql.connector

class ResourceList:

    def __init__(self):
        self.USERNAME = "altaf"
        self.PASSWORD = "toor"
        self.HOST = "127.0.0.1"
        self.connection = None

    def on_get(self, req, resp):
        if self.connection is None:
            self.connection = mysql.connector.connect( 
                host = self.HOST,
                user = self.USERNAME,
                password = self.PASSWORD 
            )
        cursor = self.connection.cursor()
        query = "SELECT timestamp, SUM(value) FROM resource GROUP BY timestamp ORDER BY timestamp;"
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        resp.status = falcon.HTTP_200
        