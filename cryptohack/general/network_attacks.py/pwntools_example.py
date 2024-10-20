from pwn import *
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)
print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

def json_recv():
    line = r.readline()
    return json.loads(line.decode())
def json_send(a):
    request = json.dumps(a).encode()
    r.sendline(request)
request = {
    "buy":"flag"
}

json_send(request)

response = json_recv()
print(response)
