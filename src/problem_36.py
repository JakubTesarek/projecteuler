#!/usr/bin/env python

"""https://projecteuler.net/problem=36"""
if __name__ == '__main__':

	result = 0
	for num in range(1000000):
		str_num = str(num)
		str_bin = str(bin(num)[2:])
		if str(int(str_num[::-1])) == str_num and str(int(str_bin[::-1])) == str_bin:
			result += num

	print(result)