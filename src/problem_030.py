#!/usr/bin/env python

def digits(num):
	digits = []

	while num:
		digits.append(num % 10)
		num /= 10

	return digits[::-1]


"""https://projecteuler.net/problem=30"""
if __name__ == '__main__':
	result = 0
	for n in range(10, (9 ** 5) * len(str((9 ** 5)))):
		if sum(i ** 5 for i in digits(n)) == n:
			result += n

	print(result)



	