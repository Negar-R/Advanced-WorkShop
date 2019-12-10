import socket
import time

IP = 'localhost'
PORT = 8210

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))
while True:
    message = client_socket.recv(1024)
    print(message.decode('utf-8'))
    msg = input('-> ')
    client_socket.send(bytes(msg, 'utf-8'))
    time.sleep(5)
