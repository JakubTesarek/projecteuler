#!/usr/bin/env python

from math_tools import primes, is_prime


"""https://projecteuler.net/problem=49"""
if __name__ == '__main__':
	for prime in primes():
		prime2 = prime + 3330
		prime3 = prime2 + 3330
		if (
			prime != 1487 and
			len(str(prime)) == 4 and
			sorted(str(prime)) == sorted(str(prime2)) == sorted(str(prime3)) and
			is_prime(prime2) and
			is_prime(prime3)
		):
			print str(prime) + str(prime + 3330) + str(prime + 6660)
			exit()