#!/usr/bin/env python

"""https://projecteuler.net/problem=39"""
if __name__ == '__main__':
	
	result_p = 0
	result_s = 0

	for p in range(1000):
		solutions = 0
		for a in range(p // 2):
			for b in range(a, (p - a) // 2):
				if (a ** 2 + b ** 2) ** 0.5 == p - a - b:
					solutions += 1

		if solutions > result_s:
			result_s = solutions
			result_p = p

	print result_p