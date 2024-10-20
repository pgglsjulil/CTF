#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import *
import json
import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level='debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(101):
    received = json_recv()

    if "flag" in received:
        print(received)
        break
    
    print("\n\n")

    print("received type = ")
    print(received["type"])
    print("received encoded value = ")
    print(received["encoded"])

    encoding = received["type"]
    word = received["encoded"]

    if encoding == "base64":
        decoded = base64.b64decode(word).decode('utf-8')
    elif encoding == "hex":
        decoded = bytes.fromhex(word).decode('utf-8')
    elif encoding == "rot13":
        decoded = codecs.decode(word, 'rot_13')
    elif encoding == "bigint":
        decoded = long_to_bytes(int(word, 16)).decode('utf-8')
    elif encoding == "utf-8":
        decoded = ''.join(chr(i) for i in word)
    
    print("DECODED: "+ decoded)
    to_send = {
        "decoded": decoded
    }
    json_send(to_send)