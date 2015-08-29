#!/usr/bin/env python

"""https://projecteuler.net/problem=54"""
if __name__ == '__main__':

	lychrel = 0
	for num in range(1, 10000):
		lychrel += 1
		for iteration in range(50):
			revnum = int(str(num)[::-1])
			num += revnum
			if str(num) == str(num)[::-1]:
				lychrel -= 1
				break

	print(lychrel)