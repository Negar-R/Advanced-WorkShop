import sqlite3


class db_connection(dbName):
    def __init__(self):
        conn = sqlite3.connect(dbName)
        return conn

    __instance = None

    def __new__(cls):
        if not A.__instance:
            A.__instance = super().__new__(cls) 
        return A.__instance


def dbQueryByParam(dbCursor, query):
    try:
        dbCursor.execute(query)
        return True
    except:
        return False


def dbQueryBylist(dbCursor, query, myList):
    try:
        dbCursor.executemany(query, myList)
        return True
    except:
        return False

        