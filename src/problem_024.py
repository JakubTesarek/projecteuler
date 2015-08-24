#!/usr/bin/env python

"""https://projecteuler.net/problem=24"""
if __name__ == '__main__':
	permutation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	max_index = len(permutation) - 1
	
	for i in range(1, 1000000):
		for k in range(max_index, -1, -1):
			if k + 1 <= max_index and permutation[k] < permutation[k + 1]:
				for s in range(max_index, k, -1):	
					if permutation[k] < permutation[s]:
						permutation[k], permutation[s] = permutation[s], permutation[k]	
						permutation[k + 1:] = permutation[:k:-1]
						break
				break

	print("".join(str(n) for n in permutation))