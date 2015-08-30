#!/usr/bin/env python

from math_tools import primes


"""https://projecteuler.net/problem="""
if __name__ == '__main__':
	primes_list = set()
	running_total = [0]

	for prime in primes(1000000):
		running_total.append(running_total[-1] + prime)
		primes_list.add(prime)


	longest_chain = 0
	chain_prime = 0
	for i in range(len(running_total) - 1, -1, -1):
		for j in range(i - 2 - longest_chain, -1, -1):
			suma = running_total[i] - running_total[j]
			if suma > 1000000:
				break

			if suma in primes_list:
				chain_length = i - j
				if longest_chain < chain_length:
					longest_chain = chain_length
					chain_prime = suma


	print(chain_prime)