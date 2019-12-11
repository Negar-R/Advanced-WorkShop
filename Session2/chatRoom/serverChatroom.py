import socket
import time
import select

#select none blicking : hamzaman hame darkhast ha ro handle mikone 
IP = ''
PORT = 8216

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen(10)
print("server up!")

socket_list = [server_socket]

clients = {}


while True:
    read_socket, write_socket, exception_socket = select.select(
        socket_list, [], socket_list)
    for s in read_socket:
        if s == server_socket: #darkhast tcp connection (server socket ye object ke ijad mishe)
            client_socket, address = server_socket.accept()
            #inja thread dorost mikonim 
            if client_socket: #bad az accept object client socket ro ijad mikone 
                client_socket.send(bytes("welcome!", 'utf-8'))
                socket_list.append(client_socket)
                user = address[0] #address[0] -> IP
                #ye function ke client socket ro behesh pass midim va ye object az addmin midim birun 
                # function ro ba thread handle mikonim 
                clients[client_socket] = user #be in object bayad bedim be ja user 
                print("Connection Established from {}".format(address))
                for client_sockets in clients:
                    if client_sockets != client_socket: #be hame gheyre khodesh mige felani join shod
                        client_sockets.send(
                            bytes("{} joined Group!".format(address), 'utf-8'))

        else:
            message = s.recv(1024)
            if not message:
                socket_list.remove(s)
                del clients[s]
                continue
          #  print(message.decode('utf-8'))
            for client_socket in clients: 
                if client_socket != s: #be hame gheyre khodesh payam mide
                    client_socket.send(message)
    for s in exception_socket:
        socket_list.remove(s)
        del clients[s]
    # print(socket_list)
# server_socket.close()
