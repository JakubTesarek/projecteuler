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


def permutations(permutation, reset=True, reverse=False):
	compare = lambda x, y : x > y if reverse else x < y

	if reset:
		permutation.sort(reverse=reverse)
	max_index = len(permutation) - 1

	done = False
	while not done:
		yield permutation
		done = True
		for k in range(max_index - 1, -1, -1):
	 		if k + 1 <= max_index and compare(permutation[k], permutation[k + 1]):
	 			done = False
	   			for s in range(max_index, k, -1):	
	   				if compare(permutation[k], permutation[s]):
	   					permutation[k], permutation[s] = permutation[s], permutation[k]	
	   					permutation[k + 1:] = permutation[:k:-1]
	   					break
	   			break


def rotations(permutation):
	for i in range(len(permutation)):
		yield permutation
		permutation.append(permutation.pop(0))


def primes(max_prime=-1):
    sieve = {}  
    num = 2  

    while True:
    	if max_prime != -1 and num >= max_prime:
    		break

        if num not in sieve:
            yield num        
            sieve[num * num] = [num]
        else:
            for p in sieve[num]:
                sieve.setdefault(p + num, []).append(p)
            del sieve[num]

        num += 1


def triangle_number(k):
	return k * (k + 1) / 2


def triagle_numbers(start=1):
	while True:
		yield triangle_number(start)
		start += 1


def pentagonal_number(k):
	return k * (3 * k - 1) / 2


def pentagonal_numbers(start=1):
	while True:
		yield pentagonal_number(start)
		start += 1


def is_pentagonal_number(num):
	return ((24 * num + 1) ** 0.5 + 1) % 6 == 0


def hexagonal_number(k):
	return k * (2 * k - 1)


def hexagonal_numbers(start=1):
	while True:
		yield hexagonal_number(start)
		start += 1