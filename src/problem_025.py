#!/usr/bin/env python

"""https://projecteuler.net/problem=25"""
if __name__ == '__main__':
	a, b = 0, 1
	cycle = 1

	while True:
		cycle += 1
		a, b = b, a + b
			
		if len(str(b)) == 1000:
			print cycle
			break