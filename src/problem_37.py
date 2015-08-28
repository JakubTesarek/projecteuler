#!/usr/bin/env python

from math_tools import primes


"""https://projecteuler.net/problem=37"""
if __name__ == '__main__':
	primes_list = []
	truncatable_primes = []

	for prime in primes():
		primes_list.append(prime)

		if len(truncatable_primes) >= 11:
			break

		prime = str(prime)
		
		if len(prime) <= 1:
			continue

		truncatable = True
		for i in range(1, len(prime)):
			if int(prime[i:]) not in primes_list or int(prime[:i]) not in primes_list:
				truncatable = False
				break

		if truncatable:
			truncatable_primes.append(int(prime))

	print(sum(truncatable_primes))