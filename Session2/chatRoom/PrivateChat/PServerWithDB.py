import socket
import time
import threading
import select
import sqlite3
from datetime import datetime

IP = ''
PORT = 5723

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen(10)
print("server up!")

socket_list = [server_socket]

clients = {}
mark = {}


# class db_connection():
#     def __init__(self):
#         pass

#     __instance = None

#     def __new__(cls):
#         if not db_connection.__instance:
#             db_connection.__instance = super().__new__(cls) 
#         return db_connection.__instance

#     def createDB(self , dbName):
#         conn = sqlite3.connect(dbName)
#         return conn 

def findContact(client_socket , user):
    conn = sqlite3.connect("PrivateChat.db")

    cursor1 = conn.cursor()
    # cursor1.execute("DROP TABLE users")
    cursor1.execute("CREATE TABLE IF NOT EXISTS users(ID INTEGER PRIMARY KEY AUTOINCREMENT , USERNAME VARCHAR(255) , CONTACT VARCHAR(255) , ONLINE VARCHAR(255) DEFAULT 'offline' , BUSY VARCHAR(255) DEFAULT 'free')")
    
    cursor1.execute("SELECT * FROM users WHERE USERNAME = ?" , (user ,))
    p = cursor1.fetchall()
    if not len(p):
        info = (user , 'online')
        cursor1.execute("INSERT INTO users(USERNAME , ONLINE) VALUES(? , ?)" , info)
        conn.commit()
    else:
        cursor1.execute("UPDATE users SET BUSY = 'free' WHERE USERNAME = ?" , (user ,))
        conn.commit()
    # test:
    cursor1.execute("SELECT * FROM users")
    p = cursor1.fetchall() 
    for i in p:
        print("In loop : " , i , type(i))

    while True:

        client_socket.send(bytes("Who do you want to chat with?", 'utf-8'))
        contact = client_socket.recv(1024).decode("utf-8")

        cursor1.execute("SELECT * FROM users WHERE USERNAME = ?" , (contact ,))
        s = cursor1.fetchall()
        if not len(s):
            client_socket.send(bytes("{} does not register".format(contact), 'utf-8'))
        else:
            if s[0][3] == 'offline': # Offline
                client_socket.send(bytes("{} is offline now".format(contact), 'utf-8'))
            else: # Online
                if s[0][2] == user: # Correct Contact
                    cursor1.execute("UPDATE users SET CONTACT = contact , BUSY = 'busy'  WHERE USERNAME = ?" , (user ,))
                    conn.commit()
                    clients[client_socket] = (user , contact)
                    client_socket.send(bytes("Start to chat with {}".format(contact), 'utf-8'))
                    return
                elif s[0][2] == None: # Online And Free 
                    cursor1.execute("UPDATE users SET CONTACT = contact  , BUSY = 'busy'  WHERE USERNAME = ?" , (user ,))
                    conn.commit()
                    clients[client_socket] = (user , contact)
                    client_socket.send(bytes("Start to chat with {}".format(contact), 'utf-8'))
                    return    
                else: # Have Another Contact
                    client_socket.send(bytes("{} is busy now".format(contact) , 'utf-8'))
                

conn = sqlite3.connect("PrivateChat.db")

cursor2 = conn.cursor()
# cursor2.execute("DROP TABLE chats")
cursor2.execute("CREATE TABLE IF NOT EXISTS chats(SENDER VAECHAR(255) , RECEIVER VARCHAR(255) , MESSAGE TEXT , DATE TEXT)")

while True:

    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
    for s in read_socket:
        if s == server_socket: 

            client_socket, address = server_socket.accept() 

            if client_socket: 

                client_socket.send(bytes("welcome!" , 'utf-8'))

                print("Connection Established from {}".format(address))

                client_socket.send(bytes("Enter Your Name : ", 'utf-8'))
                user = client_socket.recv(1024).decode("utf-8")
                
                t = threading.Thread(target = findContact , args = (client_socket , user))
                t.start()

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

                    info = (clients[client_socket][1] , clients[client_socket][0] , message.decode("utf-8") , datetime.now())
                    cursor2.execute("INSERT INTO chats(SENDER , RECEIVER , MESSAGE , DATE) VALUES(? , ? , ? , ?)" , info)
                    conn.commit()
                    # test :     
                    cursor2.execute("SELECT * FROM chats") 
                    p = cursor2.fetchall()
                    for i in p:
                        print(i)  
            
    for s in exception_socket:
        socket_list.remove(s)
        del clients[s]

server_socket.close()