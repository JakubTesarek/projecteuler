#!/usr/bin/env python

from math_tools import is_pentagonal_number, pentagonal_number


"""https://projecteuler.net/problem=44"""
if __name__ == '__main__':
	i = 0
	while True:
		i += 1
		a = pentagonal_number(i)
		for j in range(i - 1, 1, -1):
			b = pentagonal_number(j)

			if is_pentagonal_number(a - b) and is_pentagonal_number(a + b):
				print a - b
				exit()