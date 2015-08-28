#!/usr/bin/env python

"""https://projecteuler.net/problem=31"""
if __name__ == '__main__':
	coins = [1, 2, 5, 10, 20, 50, 100, 200]

	amount = 200
	cache = {}

	for y in range(0, amount + 1):
	    cache[y, 0] = 1

	for y in range(0, amount + 1):
	    for x in range(1, len(coins)):
	        cache[y, x] = 0
	        if y >= coins[x]:
	            cache[y, x] += cache[y, x - 1]
	            cache[y, x] += cache[y - coins[x], x]
	        else:
	            cache[y, x] = cache[y, x - 1]
	
	print cache[y, x]