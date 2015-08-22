#!/usr/bin/env python

def factors(n):
	factors = set([f for f in range(1, int(n ** 0.5) + 1) if n%f == 0])

	for f in set(factors):
		factors.add(n / f)

	return factors

"""https://projecteuler.net/problem=12"""
if __name__ == '__main__':
	total = 0
	n = 0

	while True:
		n += 1
		total += n

		if len(factors(total)) > 500:
			print total
			break