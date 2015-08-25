#!/usr/bin/env python

"""https://projecteuler.net/problem=28"""
if __name__ == '__main__':
	last_number = 1
	adding = 2
	sum_diagonal = 1

	while True:
		for n in range(0, 4):
			last_number += adding
			sum_diagonal += last_number

		if adding == 1000:
			break

		adding += 2

	print(sum_diagonal)