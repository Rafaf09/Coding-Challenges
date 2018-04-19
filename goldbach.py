import math
import itertools

def is_prime(num):
	"""Computes if a number is a prime, by checking primality 
	with all the numbers from 2 to n-1.


	>>> is_prime(1)
	False

	>>> is_prime(21)
	False

	>>> is_prime(47)
	True
	"""

	if num < 2:
		return False
	else:
		k = num - 1
		while k > 1:
			if num % k == 0:
				return False
			k -= 1
		return True

def sieve(num):
	"""Computes all primes less than or equal to a number,
	following the Sieve of Erathostenes.

	>>> sieve(17)
	{2, 3, 5, 7, 11, 13, 17}

	>>> sieve(50)
	{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

	>>> sieve(8)
	{2, 3, 5, 7}
	"""

	set_nums = set(range(2, num+1))
	k = 2
	while k <= math.sqrt(num):
		delete_set = set()
		for el in set_nums:
			if el % k == 0 and el != k:
				delete_set.add(el)
		k += 1
		set_nums = set_nums - delete_set
	return set_nums

def goldbach(num):
	"""Returns a group of 3 primes that sum up to a number,
	according to Goldbach's Weak Conjecture.
    
    >>> goldbach(8)
    [3, 3, 2]
    >>> goldbach(754)
    [2, 739, 13]
    >>> goldbach(70000)
    [2, 69991, 7]
    """
    
	sieve_ = sorted(sieve(num), reverse=True)
	sumands = []
	for a, b in itertools.combinations(sieve_, 2):
		if is_prime(num - (a + b)):
			sumands += [a, b]
			break
	results = [num - (sumands[0] + sumands[1]), sumands[0], sumands[1]]
	return results