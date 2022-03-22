import json
import falcon
import datetime
import mysql.connector

class Resource:

    def __init__(self):
        self.USERNAME = "altaf"
        self.PASSWORD = "toor"
        self.HOST = "192.168.131.128"
        self.connection = None

    def on_get(self, req, resp):
        timestamp = req.get_param('timestamp')
        value = req.get_param('value')
        try:
            value = int(value)
            datetime.datetime.strptime(timestamp, r'%Y-%m-%d')
        except ValueError:
            value = timestamp = None

        if timestamp and value:
            if self.connection is None:
                self.connection = mysql.connector.connect( 
                    host = self.HOST,
                    user = self.USERNAME,
                    password = self.PASSWORD 
                )
            cursor = self.connection.cursor()
            query = f"insert into lyxelnflamingo.resource values('{timestamp}',{value})"
            cursor.execute(query)
            self.connection.commit()
        resp.status = falcon.HTTP_200