import json
import mysql.connector

with open('db_credentials.json', 'r') as f:
     connection_settings = json.load(f)

mydb = mysql.connector.connect(
     host = connection_settings["host"],
     user = connection_settings["username"],
     passwd = connection_settings["password"],
     database = connection_settings["database"]
)

def getRecipieById(id):
     cursor = mydb.cursor()
     query = "SELECT name, id FROM recipe WHERE id = %s"

     cursor.execute(query, (int(id),))
     for name, id in cursor:
          print(f"{name}\tid: {id}")

getRecipieById(2)

mydb.close()
