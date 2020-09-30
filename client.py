import socket

try:
    # create new socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print(e)

# port to connect to
port = 1234

try:
    # connect to server at localhost port 1234
    s.connect(('127.0.0.1', port))

    print('Connected to localhost on port %s' % port)

    # receive data from server
    print((s.recv(1024).decode('utf-8')))
except socket.error as e:
    print(e)

