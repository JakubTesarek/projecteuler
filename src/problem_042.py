#!/usr/bin/env python

import csv


"""https://projecteuler.net/problem=42"""
if __name__ == '__main__':
	with open("fixtures/problem_042.txt", "r") as fixture:
		reader = csv.reader(fixture, delimiter=',', quotechar='"')
		words = reader.next()

	total = 0
	for word in words:
		t = sum([ord(char) - 96 for char in word.lower()])
		total += (1 + 8 * t) ** 0.5 % 2 == 1

	print(total)