#!/usr/bin/env python3

from pwn import xor
string = "label"
print(xor(string, 13).decode('utf-8'))