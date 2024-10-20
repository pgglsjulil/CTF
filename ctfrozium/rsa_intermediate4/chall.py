import sys
from Crypto.Util.number import getPrime
from libnum import s2n, n2s
from flag import FLAG

p = getPrime(2048)

pt = s2n(FLAG)

ct = pow(pt, 2**10, p)
with open("out.txt", "w+") as sys.stdout:
    print(f"{p=}")
    print(f"{ct=}")