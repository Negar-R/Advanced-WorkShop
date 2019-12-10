import sqlite3


def db_connection(dbName):
    try:
        conn = sqlite3.connect(dbName)
        return conn
    except Exception as e:
        raise e


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

        