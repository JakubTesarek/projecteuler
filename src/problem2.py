#!/usr/bin/env python

"""https://projecteuler.net/problem=2"""
if __name__ == '__main__':
	total = 0
	previous, current = 1, 2

	while current < 4000000:
		if current % 2 == 0:
			total += current
		previous, current = current, previous + current
	
	print(total)