import json
import falcon
import mysql.connector

class ResourceList:    
    def __init__(self):
        self.USERNAME = "altaf"
        self.PASSWORD = "toor"
        self.HOST = "127.0.0.1"
        self.DB = "lyxelnflamingo"
        self.TABLE = "resource"
        self.connection = None

    def __del__(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def jsonfy(self,records):
        """convert records in json format

        Args:
            records: all records that will be converted to json

        Returns:
            json string: json format records
        """        
        record_list = {"data":[]}
        for record in records:
            record_list["data"].append({"timestamp":str(record[0]), "value":int(record[1])})
        return json.dumps(record_list, ensure_ascii=False)

    def on_get(self, req, resp):
        if self.connection is None:
            self.connection = mysql.connector.connect( 
                host = self.HOST,
                user = self.USERNAME,
                password = self.PASSWORD 
            )

        cursor = self.connection.cursor()
        query = f"SELECT timestamp, SUM(value) FROM {self.DB}.{self.TABLE} GROUP BY timestamp ORDER BY timestamp;"
        cursor.execute(query)
        records = cursor.fetchall()
        resp.text = self.jsonfy(records)
        resp.status = falcon.HTTP_200
        