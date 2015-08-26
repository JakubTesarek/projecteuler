#!/usr/bin/env python

from math_tools import primes, is_pandigital


"""https://projecteuler.net/problem=41"""
if __name__ == '__main__':
	for prime in primes(7654321)[::-1]:
		if is_pandigital(prime):
			print(prime)
			break
