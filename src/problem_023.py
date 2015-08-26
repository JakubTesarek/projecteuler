#!/usr/bin/env python

from math_tools import proper_factors


"""https://projecteuler.net/problem=23"""
if __name__ == '__main__':
	abundant = []

	for n in range(1, 28124):
		if sum(proper_factors(n)) > n:
			abundant.append(n)

	numbers = set(range(1, 28124))

	for k, n in enumerate(abundant):
	 	for m in abundant[k:]:
	 		numbers.discard(m + n)
			
	print(sum(numbers))
