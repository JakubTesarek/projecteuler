#!/usr/bin/env python

"""https://projecteuler.net/problem=29"""
if __name__ == '__main__':
	results = set()

	for a in range(2, 101):
		for b in range(2, 101):
			results.add(a**b)

	print len(results)
