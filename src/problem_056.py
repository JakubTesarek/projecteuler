#!/usr/bin/env python

from math_tools import digits


"""https://projecteuler.net/problem=56"""
if __name__ == '__main__':
	result = 0

	for a in range(0, 100):
		for b in range(0, 100):
			result = max(result, sum(digits(a ** b)))


	print(result)