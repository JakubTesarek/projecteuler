#!/usr/bin/env python

"""https://projecteuler.net/problem=15"""
if __name__ == '__main__':
	# it can also be calculated using simple formula (https://en.wikipedia.org/wiki/Lattice_path) but this is more fun
	
	grid = {}

	for x in range(0, 21):
		grid[x] = {}
		for y in range(0, 21):
			if x == y == 0:
				grid[x][y] = 1
			else:
				x_value = grid[x - 1][y] if x - 1 in grid else 0
				y_value = grid[x][y - 1] if y - 1 in grid[x] else 0
				grid[x][y] = x_value + y_value

	print(grid[20][20])