#!/usr/bin/env python

def next_collatz_number(n):
	if n == 1:
		return None
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1


def collatz_len(n, seq = {}):
	if n not in seq:
		next_collatz = next_collatz_number(n)
		if next_collatz is not None:
			seq[n] = 1 + collatz_len(next_collatz, seq)
		else:
			seq[n] = 1

	return seq[n]


"""https://projecteuler.net/problem="""
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