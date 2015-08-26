#!/usr/bin/env python

from math_tools import factorial, digits


"""https://projecteuler.net/problem=34"""
if __name__ == '__main__':
	upper_bound_coef = 1
	while len(str(upper_bound_coef * factorial(9))) > upper_bound_coef:
		upper_bound_coef += 1

	result = 0

	for n in range(10, upper_bound_coef * factorial(9)):
		if sum(factorial(i) for i in digits(n)) == n:
			result += n

	print(result)
