import socket
import time

IP = ''
PORT = 8205

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen(10)

while True:
    client_socket, address = server_socket.accept()
    if client_socket:
        print("Connection Established from {}".format(address))
        client_socket.send(bytes("welcome!", "utf-8"))
       # while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            print(message)
        msg = input('-> ')
        client_socket.send(bytes(msg, "utf-8"))
#        time.sleep(5)
#    time.sleep(5)
server_socket.close()
