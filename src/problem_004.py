#!/usr/bin/env python

"""https://projecteuler.net/problem=4"""
if __name__ == '__main__':
	result = None

	for x in range(1, 999):
		for y in range(1, 999):
			prod = x * y
			if prod > result and str(prod) == str(prod)[::-1]:
				result = prod

	print(result)