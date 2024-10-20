#!/usr/bin/env python3

from pwn import xor

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
text = bytes.fromhex(hex_string)

for i in range(26):
	ans = xor(text, i).decode('utf-8')
	if ans[0:6] == 'crypto':
		print(ans)
	# print(ans)
