#!/usr/bin/env python3

from Crypto.Util.number import*
zn_ = [a for a in range(1,29) if GCD(29,a) == 1 ]
ints = [14, 6, 11]
for i in zn_:
	for j in ints:
		for k in range(1, 100):
			if pow(i,2) - j == k*29:
				print(i)
