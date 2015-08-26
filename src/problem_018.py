#!/usr/bin/env python

def row_count(graph):
	row = 0
	chars = 0
	while True:
		chars += chars_in_row(row)
		if chars >= len(graph):
			return row + 1
		row += 1


def get_num(row, column, graph):
	chars = 0
	for i in range(0, row):
		chars += chars_in_row(i)

	chars += column * 3

	return int(graph[chars:chars+2])


def numbers_in_row(row):
	return row + 1


def chars_in_row(row):
	return 3 * numbers_in_row(row)


def find_max_path_value(graph):
	node_values = {}
	rows = row_count(graph)

	for row in range(rows - 1, -1, -1):
		node_values[row] = {}
		for pos in range(0, numbers_in_row(row)):
			if row + 1 < rows:
				path_value = max(node_values[row + 1][pos], node_values[row + 1][pos + 1])
			else:
				path_value = 0
			node_values[row][pos] = get_num(row, pos, graph) + path_value

	return node_values[0][0]


"""https://projecteuler.net/problem=18"""
if __name__ == '__main__':
	graph = "\
75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

	print(find_max_path_value(graph))
