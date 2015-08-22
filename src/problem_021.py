#!/usr/bin/env python

def proper_factors(n):
	factors = set([f for f in range(2, int(n ** 0.5) + 1) if n%f == 0])

	for f in set(factors):
		factors.add(n / f)

	factors.add(1)
	return factors

def proper_factors_sum(n):
	return sum(proper_factors(n))

"""https://projecteuler.net/problem=21"""
if __name__ == '__main__':
	amicable = set()
	checked = set()

	for n in range(1, 10000):
		if n not in checked:
			checked.add(m)
			checked.add(n)

			m = proper_factors_sum(n)
			if m != n and proper_factors_sum(m) == n:
				amicable.add(m)
				amicable.add(n)

	print(sum(amicable))