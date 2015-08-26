#!/usr/bin/env python

from math_tools import is_prime


"""https://projecteuler.net/problem=3"""
if __name__ == '__main__':
	cmp = 600851475143
	print(next(div for div in xrange(int(cmp ** 0.5), 1, -1) if cmp % div == 0 and is_prime(div)))