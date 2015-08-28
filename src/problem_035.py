#!/usr/bin/env python

from math_tools import rotations, primes, is_prime

"""https://projecteuler.net/problem=35"""
if __name__ == '__main__':
	result = 0
	for prime in primes(1000000):
		result += all(is_prime(int("".join(rot))) for rot in rotations(list(str(prime))))
		
	print(result)
