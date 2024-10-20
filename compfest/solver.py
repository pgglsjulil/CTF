from pwn import *

server_address = 'ctf.rozium.cloud'
server_port = 10001

r = remote(server_address, server_port)
