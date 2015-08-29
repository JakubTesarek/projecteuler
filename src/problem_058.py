#!/usr/bin/env python

from math_tools import is_prime


"""https://projecteuler.net/problem=58"""
if __name__ == '__main__':
	side = 1
	corner = 1
	primes = 0

	while True:
		side += 2

		for i in range(4):
			corner += side - 1
			if is_prime(corner):
				primes += 1

		if (float(primes) / ((side - 1) * 2 + 1)) < 0.1:
			print(side)
			break