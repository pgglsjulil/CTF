#!/usr/bin/env python3

'''
Using the two primes p = 26513, q = 32321, find the integers u,v such that

p * u + q * v = gcd(p,q)

Enter whichever of u and v is the lower number as the flag.
'''
def extended_gcd(a, b):
	if a == 0:
		return b, 0, 1
	gcd, x1, y1 = extended_gcd(b%a, a)
	x = y1 - (b // a) *x1
	y = x1
	return gcd, x, y
if __name__ == '__main__':
	p = 26513
	q = 32321
	gcd, x, y = extended_gcd(p, q)
	print(f"gcd of {p} and {q} is {gcd}")
	print(f"u = {x} and v = {y}")
	print(f"validation {p} * {x} + {q} * {y} = {p*x + q*y}")

