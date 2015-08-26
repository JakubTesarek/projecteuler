#!/usr/bin/env python

from math_tools import proper_factors


"""https://projecteuler.net/problem=32"""
if __name__ == '__main__':
	result = 0

	for n in range(1, 10000):
		for a in proper_factors(n):
			if "".join(sorted(str(a) + str(n / a) + str(n))) == "123456789":
				result += n
				break

	print(result)