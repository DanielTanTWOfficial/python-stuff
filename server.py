import socket

s = socket.socket()

port = 1234

s.bind(('', port))
print('Socket binded to port %s' % port)

s.listen(5)
print('Socket is listening')

while True:
    c, addr = s.accept()
    print('Connection from ', addr)

    b = bytes('Thank you for connecting!', 'utf-8')

    c.send(b)

    c.close()
