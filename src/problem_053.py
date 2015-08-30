#!/usr/bin/env python

from math_tools import selections_count

"""https://projecteuler.net/problem=53"""
if __name__ == '__main__':
	count = 0

	for n in range(1, 101):
		for r in range(1, n + 1):
			if selections_count(n, r) > 1000000:
				count += 1

	print count