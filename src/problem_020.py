#!/usr/bin/env python

"""https://projecteuler.net/problem=20"""
if __name__ == '__main__':
	factorial = 1
	for n in range(1, 101):
		factorial *= n

	print(sum([int(char) for char in str(factorial)]))
