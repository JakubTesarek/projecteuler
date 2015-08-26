#!/usr/bin/env python

from math_tools import factorial, digits


"""https://projecteuler.net/problem=20"""
if __name__ == '__main__':
	print sum(digits(factorial(100)))