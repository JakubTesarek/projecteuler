#!/usr/bin/env python

from math_tools import permutations


"""https://projecteuler.net/problem=43"""
if __name__ == '__main__':
	result = 0

	for digits in permutations(["1", "0", "2", "3", "4", "5", "6", "7", "8", "9"], reset=False):
		if (
			int(digits[3]) % 2 == 0 and
			int(digits[2] + digits[3] + digits[4]) % 3 == 0 and
			int(digits[5]) % 5 == 0 and
			int(digits[4] + digits[5] + digits[6]) % 7 == 0 and
			int(digits[5] + digits[6] + digits[7]) % 11 == 0 and
			int(digits[6] + digits[7] + digits[8]) % 13 == 0 and
			int(digits[7] + digits[8] + digits[9]) % 17 == 0
		):
			result += int("".join(digits))

	print(result)