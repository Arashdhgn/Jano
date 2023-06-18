import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc


class SQL:
    def __init__(self, driver="Sql Server Native Client 11.0", server='ARASH', database="Jano"):
        self.connectionString = f"Driver={driver};" \
                               f"Server={server};" \
                               f"Database={database};" \
                               f"Trusted_connection=yes;"
        self.connection = None

    def connect(self):
        self.connection = pyodbc.connect(self.connectionString)

    def disconnect(self):
        self.connection.close()


class ShabIRSQL:
    def insert_to_Place(PlaceInfo):
        sql = SQL()
        sql.connect()
        curser = sql.connection.cursor()
        curser.execute(f"INSERT INTO Place\
                    output inserted.ID\
                    values (?, ?, ?, ?, ?, ?, ?, ?)",
                    ()
                    )



# sql = SQL()
# sql.connect()
# curser = sql.connection.cursor()
# curser.execute(f"select * from Place"
#                )
# result = curser.fetchall()
#
# print (result)