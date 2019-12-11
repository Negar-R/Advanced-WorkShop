import socket
import select
import time
# import BookList
import Member
# import Adminstrator as A

def validAdmin():
    client_socket.send(bytes("Enter Your Pass" , "utf-8"))
    for s in read_socket:
        message = s.recv(1024)
        if message.decode("utf-8") == '123':
            client_socket.send(bytes("Right Pass" , "utf-8"))
            client_socket.send(bytes("1:sign up 2:Get info" , "utf-8"))
            message = s.recv(1024).decode("utf-8")
            if message == '1':
                client_socket.send(bytes("Name" , "utf-8"))
                message = s.recv(1024).decode("utf-8")
                Member.Members(message , 20)
        else:
            client_socket.send(bytes("wrong Pass" , "utf-8")) 

IP = ''
PORT = 5010

server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server_socket.bind((IP , PORT))

server_socket.listen(10)

sockt_list = [server_socket]

clients = {}


while True:
    read_socket , write_socket , exception_socket = select.select(
        sockt_list , [] , sockt_list)
    for s in read_socket:
        if s == server_socket:
            client_socket , address = server_socket.accept() 
            if client_socket:
                client_socket.send(bytes("Welcome If you are Addminstrator print 1 else print 2" , "utf-8"))
                sockt_list.append(client_socket)
                user = address[0]
                clients[client_socket] = user
                print("Connection Established from {}".format(address)) 
        else:
            message = s.recv(1024) 
            # message = client_socket.recv(1024).decode("utf8")
            if not message:
                sockt_list.remove(s)
                del clients[s]
                continue
            print(message.decode("utf-8"))
            msg = message.decode("utf-8")
            if msg == '1':
                validAdmin()
            else:
                client_socket.send(bytes("Client" , "utf-8")) 
                client_socket.send(bytes("1:log in 2:Borrow book" , "utf-8"))
                message = s.recv(1024).decode("utf-8")
                if message == '1':
                    client_socket.send(bytes("Hi" , "utf-8")) 
                else:
                    client_socket.send(bytes("By" , "utf-8"))     
            for client_socket in clients:
                if client_socket != s:
                    client_socket.send(message)        
    for s in exception_socket:
        sockt_list.remove(s)
        del clients[s]


server_socket.close()

