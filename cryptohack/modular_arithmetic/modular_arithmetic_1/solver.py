#!/usr/bin/env python3

'''
11 ≡ x mod 6
8146798528947 ≡ y mod  17
'''
a = 11 % 6
b = 8146798528947 % 17
print(a if a < b else b)