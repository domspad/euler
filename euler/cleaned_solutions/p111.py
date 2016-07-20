
# 105 with debugging...
# In [74]: %time %run p111.py
# 612407567715
# CPU times: user 2.92 s, sys: 23.1 ms, total: 2.94 s
# Wall time: 2.95 s


from math import sqrt

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

# only need primes up to sqrt(10**11)
UB = int(sqrt(10**11))+1
PRIMES = primes_lt3(UB)

import bisect

def is_prime(n):
	"""
	check if n is prime
	req: 1 < n < 10**11
	"""
	limit = int(sqrt(n)) + 1
	limit_idx = bisect.bisect(PRIMES, limit) + 1
	return not any( (n % p == 0 for p in PRIMES[:limit_idx]))


from itertools import product, combinations

# finding M(n,d)


def n_dig_r_dpeats(n,d,r):
	"""
	all n-digit numbers with 'd' repeated n times
	"""
	digits = [d]*n
	num_fill = n-r
	# for all places of fill-ins
	for idxs in combinations(xrange(n), num_fill):
		# try all fill-ins
		for fillins in product(*(xrange(10) for i in xrange(num_fill))):
			digits = [d]*n
			# no extra d's
			if d in fillins:
				continue
			for idx, fillin in zip(idxs,fillins):
				digits[idx] = fillin

			# num can't start with 0
			if digits[0] == 0:
				continue
			else:
				yield int(''.join(map(str,digits)))

def M(N,d):
	"""
	return maximum number of repeated digits 'd' in N-digit number which is still prime
	"""
	for r in xrange(N,-1,-1):
		if any( is_prime(cand) for cand in n_dig_r_dpeats(N,d,r)):
			return r

def N(N,d):
	m = M(N,d)
	return len(filter(is_prime, n_dig_r_dpeats(N,d,m)))

def S(N,d):
	m = M(N,d)
	return sum(filter(is_prime, n_dig_r_dpeats(N,d,m)))

print sum(S(10,d) for d in xrange(10))
#
# OLD BUGGY....
#

# def num_perm_gen(N, buffs, digits):
# 	places = permutations(xrange(N),len(digits))
# 	for idxs in places:
# 		num = [buffs[0]]*N
# 		for idx, d in zip(idxs,digits):
# 			num[idx] = d

# 		# cannot start with 0
# 		if num[-1] == 0:
# 			continue
# 		else:
# 			yield int(''.join(map(str,reversed(num))))

# g = num_perm_gen(4,(5,5),(1,2))
# assert len([i for i in g]) == len(set(permutations((5,5,1,2))))



# def repeated_num_primes(N,d,num_buffs):
# 	"""
# 	list of all N-digit primes numbers with digit 'd' repeated exactly 'num_buffs' times
# 	"""
# 	num_digits = N - num_buffs
# 	buffs = (d,)*num_buffs
# 	nums = []
# 	candigits = range(10)
# 	candigits.pop(d)
# 	for digits in combinations(candigits,num_digits):
# 		for num in num_perm_gen(N, buffs, digits):
# 			if is_prime(num):
# 				nums.append(num)
# 	return nums

# def M(N,d):
# 	"""
# 	return maximum number of repeated digits 'd' in N-digit number which is still prime
# 	"""
# 	for num_buffs in xrange(N,-1,-1):
# 		buffs = (d,)*num_buffs
# 		num_digits = N - num_buffs
# 		for digits in combinations(xrange(10),num_digits):
# 			for num in num_perm_gen(N, buffs, digits):
# 				if is_prime(num):
# 					# print num
# 					return num_buffs


# def N(N,d):
# 	num_buffs = M(N,d)
# 	return len(repeated_num_primes(N,d,num_buffs))


# def S(N,d):

# 	num_buffs = M(N,d)
# 	return sum(set(repeated_num_primes(N,d,num_buffs)))

# print 4, sum(S(4,d) for d in xrange(10))
# print 10, sum(S(10,d) for d in xrange(10))