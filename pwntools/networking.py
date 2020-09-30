from pwn import *

io = remote('google.com', 80)
io.send('GET /\r\n\r\n')
io.recvline()