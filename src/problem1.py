#!/usr/bin/env python

"""https://projecteuler.net/problem=1"""
if __name__ == '__main__':
	print(sum([n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0]))