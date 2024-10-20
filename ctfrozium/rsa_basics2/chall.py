import sys
from Crypto.Util.number import getPrime
from libnum import s2n, n2s
from flag import FLAG

p = getPrime(512)
q = getPrime(512)

n = p * q

pt = s2n(FLAG)
ct = pow(pt, 0x10001, n)
with open("out.txt", "w+") as sys.stdout:
    print(f"{n=}")
    print(f"{p=}")
    print(f"{ct=}")