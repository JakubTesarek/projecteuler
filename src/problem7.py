#!/usr/bin/env python

"""https://projecteuler.net/problem=7"""
if __name__ == '__main__':
	primes = []

	i = 2
	while len(primes) < 10001:
		if all(i % prime != 0 for prime in primes):
			primes.append(i)
		i += 1

	print(primes[-1])