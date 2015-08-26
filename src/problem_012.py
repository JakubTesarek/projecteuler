#!/usr/bin/env python

from math_tools import factors


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