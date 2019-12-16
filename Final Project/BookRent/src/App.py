import socket
import time
import select
import threading
import sqlite3
import BookList
import Adminstrator

IP = ''
PORT = 5734

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen(10)
print("server up!")

socket_list = [server_socket]

clients = {}

conn = BookList.Member.sqlite3.connect('Library.db')
cursor = conn.cursor()

def check(tableName, username):
    # conn = sqlite3.connect("Library.db")
    # cursor = conn.cursor()

    cursor.execute("SELECT * FROM admins WHERE NAME = ?" , (username ,))
    s = cursor.fetchone()
    if s:
        return True

    return False

def captcha():
    pass


def adminLogin(client_socket):

    while True:
        client_socket.send(bytes("1:Add Member , 2:Add Book, 3:Add Admin, 4:GetInformation of book, 5:Tamdid Zaman 6:Remove Book , 7:Rent Book , 8:Who Have Book", 'utf-8'))
        msg = client_socket.recv(1024).decode("utf-8")

        if msg == '1':
            client_socket.send(bytes("Name, Age", 'utf-8'))
            msg = client_socket.recv(1024).decode("utf-8")
            info_l = msg.split(",")
            
            m = BookList.Member.Members(info_l[0] , int(info_l[1]))
            m.addMember()

            cursor.execute("SELECT * FROM members")
            s = cursor.fetchall()

            for i in s:
                print(i)

        elif msg == '2':   
            client_socket.send(bytes("Name, Author , Category , International ,  BookId , Count", 'utf-8'))
            msg = client_socket.recv(1024).decode("utf-8")
            info_l = msg.split(",") 

            b = BookList.Book(info_l[0] , info_l[1] , info_l[2] , info_l[3] , info_l[4] , int(info_l[5]))
            b.addBook()

            cursor.execute("SELECT * FROM books")
            s = cursor.fetchall()

            for i in s:
                print(i)

        elif msg == '3':

            client_socket.send(bytes("Name, Age", 'utf-8'))
            msg = client_socket.recv(1024).decode("utf-8")
            info_l = msg.split(",")
            
            m = BookList.Member.Members(info_l[0] , int(info_l[1]))
            m.addAdmin()

            cursor.execute("SELECT * FROM admins")
            s = cursor.fetchall()

            for i in s:
                print(i)

        elif msg == '4':

            client_socket.send(bytes("Enter Id of the book", 'utf-8'))
            bookId = client_socket.recv(1024).decode("utf-8")

            cursor.execute("SELECT * FROM books WHERE BOOKID = ?" , (bookId ,))
            s = cursor.fetchall()

            for i in s:
                print(s)

        elif msg == '5':
            pass

        elif msg == '6':
            client_socket.send(bytes("Name, Author , Category , International ,  BookId , Count", 'utf-8'))
            msg = client_socket.recv(1024).decode("utf-8")
            info_l = msg.split(",") 

            b = BookList.Book(info_l[0] , info_l[1] , info_l[2] , info_l[3] , info_l[4] , int(info_l[5]))
            b.removeBook()

            cursor.execute("SELECT * FROM books")
            s = cursor.fetchall()

            for i in s:
                print(i)

        elif msg == '7':
            client_socket.send(bytes("Enter Id of the book", 'utf-8'))
            g = client_socket.recv(1024).decode("utf-8")

            b = BookList.Book.whoHaveBook(g)

        else:
            pass
            

def memberLogin(client_socket):

    while True:
        print("Salam !!")
        client_socket.send(bytes("1:List of  borrowed book 2:Get Information of book 3:exit" , 'utf-8'))
        msg = client_socket.recv(1024).decode("utf-8")

        if msg == '1':
            client_socket.send(bytes("Enter your Id", 'utf-8'))
            iD = client_socket.recv(1024).decode("utf-8")

            # a = Adminstrator.Admin()
            # a.getListOfBorrowedBook(msg)
            cursor.execute("SELECT BORROWEDBOOK FROM members WHERE ID = ?" , (iD ,))
            s = cursor.fetchall()
            
            print(s)

        elif msg == '2':
            client_socket.send(bytes("Enter Id of the book", 'utf-8'))
            bookId = client_socket.recv(1024).decode("utf-8")

            cursor.execute("SELECT * FROM books WHERE BOOKID = ?" , (bookId ,))
            s = cursor.fetchall()

            for i in s:
                print(s)

        else:
            break    


def askCircumstance(client_socket):

    flag = False
    cnt  = 0
    while not flag:
        client_socket.send(bytes("1 : Admin or 2 : Member", 'utf-8'))
        msg1 = client_socket.recv(1024).decode("utf-8")

        client_socket.send(bytes("username", 'utf-8'))
        msg2 = client_socket.recv(1024).decode("utf-8")
        # msg2.split(',')

        if msg1 == '1':
            # while cnt < 3:
            #     if check("admins", msg2):
            adminLogin(client_socket)
            #         flag = True
            #         break
            #     else:
            #         cnt += 1
            # if cnt == 3:
            #     # captcha(client_socket)      
            #     pass   

            # t1 = threading.Thread(target = adminLogin , args = (client_socket,))
            # t1.start()
        
        else:
            # while cnt < 3:
            #     if check("members", msg2):
            memberLogin(client_socket)
            #         flag = True
            #         break
            #     else:
            #         cnt += 1
            # if cnt == 3:
            #     # captcha(client_socket)
            #     pass


while True:
    read_socket, write_socket, exception_socket = select.select(socket_list, [], socket_list)

    for s in read_socket:
        if s == server_socket:

            client_socket, address = server_socket.accept() 
            if client_socket:  

                client_socket.send(bytes("welcome!", 'utf-8'))
                
                print("Connection Established from {}".format(address))

                # t = threading.Thread(target = askCircumstance, args = (client_socket,))
                # t.start()
                askCircumstance(client_socket)

                socket_list.append(client_socket)
    
        else:
            try:
                message = s.recv(1024)
            except:
                # if not message:
                print("NOt message")
                try:
                    socket_list.remove(s)
                    del clients[s]
                except:
                    pass
                continue
            else:
                # client_socket = findReceiver(s)
                client_socket.send(message)
            
    for s in exception_socket:
        try:
            socket_list.remove(s)
            del clients[s]
        except:
            pass
    time.sleep(2)

conn.close()
# server_socket.close()