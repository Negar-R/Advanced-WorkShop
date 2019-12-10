import socket
import time
import threading
import select
import sqlite3
from datetime import datetime

IP = ''
PORT = 5721

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen(10)
print("server up!")

socket_list = [server_socket]

clients = {}
mark = {}


class db_connection():
    def __init__(self):
        pass

    __instance = None

    def __new__(cls):
        if not A.__instance:
            A.__instance = super().__new__(cls) 
        return A.__instance

    def createDB(self , dbName):
        conn = sqlite3.connect(dbName)
        return conn 


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

def findContact(client_socket , user , conn , cursor1):
    while True:

        print("in find contact")

        client_socket.send(bytes("Who do you want to chat with?", 'utf-8'))
        contact = client_socket.recv(1024).decode("utf-8")

        Query = "SELECT USERNAME FROM users"
        dbQuery = dbQueryByParam(cursor1 , Query)
        if contact not in dbQuery:
            client_socket.send(bytes("{} does not register".format(contact), 'utf-8'))

        else:
            Query = "SELECT CONTACT FROM users WHERE USERNAME = contact"
            dbQuery = dbQueryByParam(cursor1 , Query)
            if user in Query:
                # mark[user] = contact
                Query1 = "UPDATE users SET CONTACT = contact , BUSY = TRUE WHERE USERNAME = user"
                dbQuery = dbQueryByParam(cursor1 , Query1)
                if dbQuery:
                    conn.commit()
                clients[client_socket] = (user , contact)
                client_socket.send(bytes("Start to chat with {}".format(contact), 'utf-8'))
            else:
                Query = "SELECT BUSY FROM users WHERE USERNAME = contact"
                if Query == True:
                    client_socket.send(bytes("{} is busy now".format(contact) , 'utf-8'))

            Query = "SELECT STATUS FROM users WHERE USERNAME = contact"
            dbQuery = dbQueryByParam(cursor1 , Query)
            if Query == False:
                client_socket.send(bytes("{} is offline now".format(contact), 'utf-8'))

            Query = "SELECT STATE , BUSY FROM users WHERE USERNAME = contact"
            if Query[0] == True and Query[1] == False:
                Query1 = "UPDATE users SET CONTACT = contact , BUSY = TRUE WHERE USERNAME = user"
                dbQuery = dbQueryByParam(cursor1 , Query1)
                if dbQuery:
                    conn.commit()
                clients[client_socket] = (user , contact)
                client_socket.send(bytes("Start to chat with {}".format(contact), 'utf-8'))



dconn = db_connection()
conn = dconn.createDB("PrivateChat.db")

cursor1 = conn.cursor()
Query = "CREATE TABLE IF NOT EXISTS users(ID PRIMARY KEY AUTOINCREMENT , USERNAME VARCHAR(255) , CONTACT VARCHAR(255) , ONLINE BOOLEAN , STATE VARCHAR(255)"
dbQueryByParam(cursor1 , Query)



cursor2 = conn.cursor()
Query = "CREATE TABLE IF NOT EXISTS chats(SENDER VAECHAR(255) , RECIVER VARCHAR(255)) , MESSAGE TEXT , DATE TEXT"
dbQueryByParam(cursor2 , Query)



while True:

    print("in the begining of while")

    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
    for s in read_socket:
        if s == server_socket: 

            print("tcp connection")

            client_socket, address = server_socket.accept() 

            if client_socket:  

                print("in client_socket")

                client_socket.send(bytes("welcome!" , 'utf-8'))

                print("Connection Established from {}".format(address))

                client_socket.send(bytes("Enter Your Name : ", 'utf-8'))
                user = client_socket.recv(1024).decode("utf-8")

                #mark[user] = 1
                Query = "INSERT INTO users(USERNAME , ONLINE) VALUES(? , ?)"
                info = (user , True)
                dbQuery = dbQueryBylist(cursor1 , Query , info)
                
                t = threading.Thread(target = findContact , args = (client_socket , user , conn , cursor1))
                t.start()

                print("After thread")

                socket_list.append(client_socket)
                addr = address[0] 
        else:
            message = s.recv(1024)
            if not message:
                socket_list.remove(s)
                del clients[s]
                continue
            for client_socket in clients.keys():
                if clients[client_socket][0] == clients[s][1]:
                    client_socket.send(message)
                    Query = "INSERT INTO chats(SENDER , RECIEVER , MESSAGE , DATE) VALUES(? , ? , ? , ?)"
                    info = (clients[client_socket][0] , clients[client_socket][1] , message , datetime.now())
                    dbQuery = dbQueryByParam(cursor2 , Query , info)
                    if dbQuery:
                        conn.commit()
                    #test :     
                    Query = "SELECT * FROM chats"
                    dbQueryByParam(cursor2 , Query)    
            
    for s in exception_socket:
        socket_list.remove(s)
        del clients[s]

server_socket.close()