#!/usr/bin/env python

"""https://projecteuler.net/problem=5"""
if __name__ == '__main__':
	primes = []
	result = 1

	for x in range(1, 21):
		for prime in primes:
			if x % prime == 0:
				x /= prime
		primes.append(x) # not really primes, we use number 1 too
		result *= x
		
	print(result)