#!/usr/bin/env python

from math_tools import proper_factors


def proper_factors_sum(num):
	return sum(proper_factors(num))


"""https://projecteuler.net/problem=21"""
if __name__ == '__main__':
	amicable = set()
	checked = set()

	for n in range(1, 10000):
		if n not in checked:
			m = proper_factors_sum(n)
			checked.add(m)
			checked.add(n)

			if m != n and proper_factors_sum(m) == n:
				amicable.add(m)
				amicable.add(n)

	print(sum(amicable))