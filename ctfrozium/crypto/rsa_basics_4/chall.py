import sys
from Crypto.Util.number import getPrime
from libnum import s2n, n2s
from flag import FLAG

n = 1
st = getPrime(15)
while n.bit_length() < 1024:
    n *= st
    st = getPrime(15)

pt = s2n(FLAG)

ct = pow(pt, 0x10001, n)
with open("out.txt", "w+") as sys.stdout:
    print(f"{n=}")
    print(f"{ct=}")