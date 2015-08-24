#!/usr/bin/env python

import csv

"""https://projecteuler.net/problem=22"""
if __name__ == '__main__':
	with open("fixtures/problem_022.txt", "r") as fixture:
		reader = csv.reader(fixture, delimiter=',', quotechar='"')
		names = reader.next()

	result = 0

	for key, name in enumerate(sorted(names)):
		result += (key + 1) * sum([ord(char) - 96 for char in name.lower()])

	print result