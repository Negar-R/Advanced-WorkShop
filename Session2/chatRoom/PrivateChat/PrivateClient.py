import socket
import time
import sys
import threading

# IP = '192.168.43.66'
IP = 'localhost'
PORT = 5722
#username = input("Enter your name: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(1)


def send_message():
    while True:
        msg = input()
        if msg:
            client_socket.send(bytes(msg, 'utf-8'))


t1 = threading.Thread(target=send_message)
t1.start()

# t2 = threading.Thread(target=hello)
# t2.start()


while True:
    # #    message = client_socket.recv(1024)
    # #    print(message.decode('utf-8'))
    # msg = input('{}-> '.format(username))
    # if msg:
    #     client_socket.send(bytes(username + "->" + msg, 'utf-8'))

    try:
        while True:
            message = client_socket.recv(1024)
            if not message: 
                # in ja faghat nemiad message ro begire
                # balke recv miad barresi  ham mikone ke connection hast ya ghat shode
                print("Connection Closed!")
                sys.exit()
            print(message.decode('utf-8'))

    except IOError as e:
        # print("Error")
        # pass
        raise e

#    time.sleep(5)