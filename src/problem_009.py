#!/usr/bin/env python

"""https://projecteuler.net/problem=9"""
if __name__ == '__main__':
	for a in range(333, 999):
		for b in range(1, 1000 - 333 - a):
			c = 1000 - a - b
			if a ** 2 == b ** 2 + c ** 2:
				print(a * b * c)
				
