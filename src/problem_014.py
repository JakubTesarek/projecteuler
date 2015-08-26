#!/usr/bin/env python

from math_tools import collatz_len


"""https://projecteuler.net/problem=14"""
if __name__ == '__main__':
	seq = {}

	max_len_seq = None
	max_len_gen = None

	for gen in range(1, 1000000):
		chain_len = collatz_len(gen, seq)
		if chain_len > max_len_seq:
			max_len_seq = chain_len
			max_len_gen = gen

	print(max_len_gen)