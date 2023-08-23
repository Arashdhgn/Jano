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
    def PlaceInfoInsert(self,PlaceInfo):
        sql = SQL()
        sql.connect()
        curser = sql.connection.cursor()
        curser.execute(f"INSERT INTO PlacesInfo\
                        values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,GETDATE())",
                        (PlaceInfo[0],
                         PlaceInfo[1],
                         PlaceInfo[2],
                         PlaceInfo[3],
                         PlaceInfo[4],
                         PlaceInfo[5],
                         PlaceInfo[6],
                         PlaceInfo[7],
                         PlaceInfo[8],
                         PlaceInfo[9],
                         PlaceInfo[10],
                         PlaceInfo[11],
                         PlaceInfo[12],
                         PlaceInfo[13])
                        )
        curser.commit()

    def PlaceCalendarInfoInsert(self,PlaceInfo):
        sql = SQL()
        sql.connect()
        curser = sql.connection.cursor()
        curser.execute(f"INSERT INTO PlaceCalendarInfo\
                        values (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (PlaceInfo[0],
                        PlaceInfo[1],
                        PlaceInfo[2],
                        PlaceInfo[3],
                        PlaceInfo[4],
                        PlaceInfo[5],
                        PlaceInfo[6],
                        PlaceInfo[7],
                        PlaceInfo[8],
                        PlaceInfo[9],
                        PlaceInfo[10],
                        PlaceInfo[11])
                        )
        curser.commit()



# sql = SQL()
# sql.connect()
# curser = sql.connection.cursor()
# curser.execute(f"select * from Place"
#                )
# result = curser.fetchall()
#
# print (result)