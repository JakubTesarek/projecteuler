#!/usr/bin/env python

from math_tools import primes


"""https://projecteuler.net/problem=46"""
if __name__ == '__main__':
	primes_list = []
	num = 9
	for next_prime in primes():
		while num < next_prime:
			if num not in primes_list:
				found = False
				for prime in primes_list:
					if ((num - prime) / 2) ** 0.5 % 1 == 0:
						found = True
						break

				if not found:
					print(num)
					exit()
					
			num += 2
		primes_list.append(next_prime)