#!/usr/bin/env python

from problem_018 import find_max_path_value

"""https://projecteuler.net/problem="""
if __name__ == '__main__':
	with open("fixtures/problem_067.txt", "r") as fixture:
		graph=fixture.read()

	print find_max_path_value(graph)