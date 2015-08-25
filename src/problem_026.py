#!/usr/bin/env python

"""https://projecteuler.net/problem=26"""
if __name__ == '__main__':

	longest_number = 0
	period_len = 0

	for i in range(1, 1000):
		decimals = []
		reminders = set()
	
		numerator = 1
		denominator = i

		while True:
			if numerator not in reminders:
				reminders.add(numerator)
			else:
				break

			decimal = numerator / denominator
			numerator = numerator % denominator

			if numerator == 0:
				decimals = []
				break

			if decimal == 0:
				numerator *= 10
			else:
				decimals.append(decimal)

		if len(decimals) > period_len:
			period_len = len(decimals)
			longest_number = i

	print(longest_number)