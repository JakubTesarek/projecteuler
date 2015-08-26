#!/usr/bin/env python

def number_of_days(month, year):
	if month in [4, 6, 9, 11]:
		return 30
	elif month in [1, 3, 5, 7,  8, 10, 12]:
		return 31
	elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		return 29
	else:
		return 28


def next_month(month, year):
	month = month % 12 + 1
	if month == 1:
		year += 1

	return month, year


"""https://projecteuler.net/problem=19"""
if __name__ == '__main__':
	weekday, day, month, year = 1, 1, 1, 1900
	first_sundays = 0

	while year <= 2000:
		if year >= 1901 and weekday == 7:
			first_sundays += 1

		weekday = (weekday + number_of_days(month, year) - 1) % 7 + 1
		month, year = next_month(month, year)

	print(first_sundays)