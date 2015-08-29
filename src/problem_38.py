#!/usr/bin/env python

from math_tools import permutations

"""https://projecteuler.net/problem=38"""
if __name__ == '__main__':
	for permutation in permutations(["9", "8", "7", "6", "5", "4", "3", "2", "1"], reverse=True, reset=False):
		for num_chars in range(0, len(permutation) // 2):
			counter = 1
			sequence = "".join(permutation)
			base = int(sequence[0:num_chars + 1])
			while True:
				base_w = str(base * counter)

				if not sequence.startswith(base_w):
					break

				sequence = sequence[len(base_w):]
				counter += 1

			if len(sequence) == 0:
				print("".join(permutation))
				exit()