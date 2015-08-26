from itertools import count, islice


def factorial(num, cache = {}):
	if num not in cache:
		factorial = 1
		for n in range(1, num + 1):
			factorial *= n
		cache[num] = factorial

	return cache[num]


def digits(num):
	digits = []

	while num:
		digits.append(num % 10)
		num /= 10

	return digits[::-1]


def proper_factors(num):
	factors = set([f for f in range(2, int(num ** 0.5) + 1) if num % f == 0])

	for f in set(factors):
		factors.add(num / f)

	factors.add(1)
	return factors


def factors(num):
	factors = proper_factors(num)
	factors.add(num)
	return factors


def primes(max):
	exclude = set()
	primes = []

	x = 2
	while x < max + 1:
		if x not in exclude:
			primes.append(x)
			i = x
			while i < max + 1:
				exclude.add(i)
				i += x
		x += 1

	return primes


def is_prime(num):
	if num < 2: return False
	return all(num % i for i in islice(count(start=2), int(num ** 0.5 - 1)))


def next_collatz_number(num):
	if num == 1:
		return None
	if num % 2 == 0:
		return num / 2
	else:
		return 3 * num + 1


def collatz_len(num, seq = {}):
	if num not in seq:
		next_collatz = next_collatz_number(num)
		if next_collatz is not None:
			seq[num] = 1 + collatz_len(next_collatz, seq)
		else:
			seq[num] = 1

	return seq[num]


def is_pandigital(num):
	return not cmp(sorted(digits(num)), range(1, len(str(num)) + 1))