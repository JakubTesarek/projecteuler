#!/usr/bin/env python

from problem_010 import primes
from problem_003 import is_prime

"""https://projecteuler.net/problem=27"""
if __name__ == '__main__':
	
	generator_product = None
	max_primes_generated = None

	for b in primes(1000):
		for a in range(-999, 1000, 2):
			n = 0
			primes_generated = 0
			while True:
				if not is_prime((n ** 2) + (a * n) + b):
					break

				primes_generated += 1
				n += 1
			
			if primes_generated > max_primes_generated:
				max_primes_generated = primes_generated
				generator_product = a * b

	print(generator_product)