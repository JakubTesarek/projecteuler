#!/usr/bin/env python

from math_tools import triagle_numbers, pentagonal_numbers, hexagonal_numbers

"""https://projecteuler.net/problem=45"""
if __name__ == '__main__':
	triagle_numbers = triagle_numbers(start=286)
	pentagonal_numbers = pentagonal_numbers(start=166)
	hexagonal_numbers = hexagonal_numbers(start=144)

	triagle = triagle_numbers.next()
	pentagonal = pentagonal_numbers.next()
	hexagonal = hexagonal_numbers.next()
	
	while True:
		if triagle == pentagonal == hexagonal:
			print triagle
			break
		elif triagle <= min(pentagonal, hexagonal):
			triagle = triagle_numbers.next()
		elif pentagonal <= min(triagle, hexagonal):
			pentagonal = pentagonal_numbers.next()
		else:
			hexagonal = hexagonal_numbers.next()