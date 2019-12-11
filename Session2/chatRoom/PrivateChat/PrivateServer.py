import socket
import time
import select
import threading

#select none blicking : hamzaman hame darkhast ha ro handle mikone
#0 : offline , 1 : online , 2 : busy
IP = ''
PORT = 1235

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen(10)
print("server up!")

socket_list = [server_socket]

clients = {}
mark = {}

def findContact(client_socket,user):
    while True:
        client_socket.send(bytes("Who do you want to chat with?", 'utf-8'))
        contact = client_socket.recv(1024).decode("utf-8")

        if contact not in mark:
            client_socket.send(bytes("{} does not register".format(contact), 'utf-8'))
            # print('inja 01')
            # print("mark",mark)
            # print("contact",contact)
        elif type(mark[contact]) == type(" string "): #busy
            # print("inja 02")
            # print("mark",mark)
            if mark[contact] == user:
                # print("inja 03")
                # print("mark",mark)
                mark[user] = contact
                clients[client_socket] = (user , contact)
                client_socket.send(bytes("Start to chat with {}".format(contact), 'utf-8'))
                return
                
            else :
                # print("inja 04")
                # print("mark" , mark)
                client_socket.send(bytes("{} is busy now".format(contact) , 'utf-8'))
        elif mark[contact] == 0:
            # print("inja 05")
            # print("mark",mark)
            
            client_socket.send(bytes("{} is offline now".format(contact), 'utf-8'))

        elif mark[contact] == 1:
            # print("inja 06")
            # print("mark",mark)
            mark[user] = contact
            clients[client_socket] = (user , contact)
            client_socket.send(bytes("Start to chat with {}".format(contact), 'utf-8'))
            return


while True:
    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
    # print("saa " , read_socket)

    for s in read_socket:
        if s == server_socket: #darkhast tcp connection (server socket ye object ke ijad mishe)
            # print("In if --------------------")
            client_socket, address = server_socket.accept() 
            if client_socket:  

                client_socket.send(bytes("welcome!", 'utf-8'))

                print("Connection Established from {}".format(address))

                client_socket.send(bytes("Enter Your Name : ", 'utf-8'))
                user = client_socket.recv(1024).decode("utf-8")

                mark[user] = 1
                
                t = threading.Thread(target = findContact , args = (client_socket,user))
                t.start()

                socket_list.append(client_socket)
                addr = address[0] 
                # print(mark) 
                # clients[client_socket] = (user , contact)
            
                # print("Done here")
                # print(clients)

        else:
            # print("in else ________________-")
            message = s.recv(1024)
            if not message:
                # print("NOt message")
                socket_list.remove(s)
                del clients[s]
                continue

            # print("refighet -- > " , clients[s][1])
            # print("dustam -- > " , message.decode('utf-8'))
            for client_socket in clients.keys():
                # print(clients[client_socket][0])
                if clients[client_socket][0] == clients[s][1]:
                    client_socket.send(message)
            
    for s in exception_socket:
        # print("In exception")
        socket_list.remove(s)
        del clients[s]
    # print(socket_list)
server_socket.close()