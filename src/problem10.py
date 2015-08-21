#!/usr/bin/env python

"""https://projecteuler.net/problem=10"""
if __name__ == '__main__':
	exclude = set()
	primes = set()

	x = 2
	while x < 2000000:
		if x not in exclude:
			primes.add(x)
			i = x
			while i < 2000000:
				exclude.add(i)
				i += x
		x += 1

	print(sum(primes))