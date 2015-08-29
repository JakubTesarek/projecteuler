#!/usr/bin/env python



"""https://projecteuler.net/problem=52"""
if __name__ == '__main__':

	i = 0
	while True:
		i += 1
		if sorted(str(i * 2)) == sorted(str(i * 3)) == sorted(str(i * 4)) == sorted(str(i * 5)) == sorted(str(i * 6)):
			print(i)
			break