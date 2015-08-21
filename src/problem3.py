#!/usr/bin/env python

from itertools import count, islice

def is_prime(n):
	if n < 2: return False
	return all(n % i for i in islice(count(start=2), int(n ** 0.5 - 1)))


"""https://projecteuler.net/problem=3"""
if __name__ == '__main__':
	cmp = 600851475143
	print(next(div for div in xrange(int(cmp ** 0.5), 1, -1) if cmp % div == 0 and is_prime(div)))