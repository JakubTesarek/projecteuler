#!/usr/bin/env python

"""https://projecteuler.net/problem=40"""
if __name__ == '__main__':
	buff = ""
	num = 0

	while len(buff) < 1000000:
		num += 1
		buff += str(num)

	print(
		int(buff[1 - 1]) *
		int(buff[10 - 1]) *
		int(buff[100 - 1]) *
		int(buff[1000 - 1]) *
		int(buff[10000 - 1]) *
		int(buff[100000 - 1]) *
		int(buff[1000000 - 1])
	)