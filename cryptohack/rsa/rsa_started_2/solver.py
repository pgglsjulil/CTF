#!/usr/bin/env python3

#common e is 0x10001 and 65537

m = 12
e = 65537
p = 17
q = 23

N = p*q

encrypt_message = pow(m, e, N)
print(encrypt_message)
