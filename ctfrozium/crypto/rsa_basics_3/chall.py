import sys
from Crypto.Util.number import getPrime
from libnum import s2n, n2s
from flag import FLAG

p = getPrime(512) # 512 bit
q = getPrime(512) # 512 bit

n = p * q # 1024

pt = s2n(FLAG)
assert(pt.bit_length() < 300) # 300 bit
ct = pow(pt, 3, n) # 900 bit
with open("out.txt", "w+") as sys.stdout:
    print(f"{n=}")
    print(f"{ct=}")