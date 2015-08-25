#!/usr/bin/env python

def primes(max):
	exclude = set()
	primes = []

	x = 2
	while x < max + 1:
		if x not in exclude:
			primes.append(x)
			i = x
			while i < max + 1:
				exclude.add(i)
				i += x
		x += 1

	return primes

"""https://projecteuler.net/problem=10"""
if __name__ == '__main__':
	print(sum(get_primes(2000000)))