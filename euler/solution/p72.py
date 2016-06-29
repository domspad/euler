



# first wanna get formula for phi...

#from prob p71
def gcd(a,b):
	"""
	a >= 0 int
	b > a int
	"""
	while a != 0 and a != 1:
		a, b = b - ((b / a) * a), a
	if a == 0:
		return b
	elif a == 1:
		return 1
	else:
		print "uh-oh!"


#from prob 10
from math import sqrt
def primes_ltn(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

### with factorization
#### with help from earlier probs... 59 + run time (15mins)
# In [1]: %time %run p72.py
# 303963552391
# CPU times: user 15min 5s, sys: 1.82 s, total: 15min 7s
# Wall time: 15min 9s

	# 10 ** 4
		# 30397485
	# 	CPU times: user 315 ms, sys: 9.43 ms, total: 325 ms
	# 	Wall time: 319 ms		
	# 10 ** 5
		# 3039650753
		# CPU times: user 15.5 s, sys: 57.2 ms, total: 15.6 s
		# Wall time: 15.6 s
	# 10 ** 6
		#303963552391
		# CPU times: user 15min 5s, sys: 1.82 s, total: 15min 7s
		# Wall time: 15min 9s


N = (10 ** 6) + 1
PRIMES = primes_ltn(N)

def factorize(n):
	"""
	12 --> ((2,2),(3,2))
	"""
	# primes = primes_ltn(n)
	factors = []
	for p in PRIMES:
		i = 0
		while n % p == 0:
			n = n / p
			i += 1
		if i > 0:
			factors.append((p,i))
		if n == 1:
			return factors
	return factors

def brute_phi(n):
	return len([i for i in xrange(1,n) if gcd(i,n) == 1])

def phi_factors(n):
	"""
	phi(10) =  4 == (2-1)*(5-1)
	phi(p^k) == 		p^(k-1) if k>1 else p-1
	phi(pq) == 			(p-1)*(q-1)
	phi((p^k)q) ==		p^(k-1)*(q-1)
	phi((p^k)(q^j)) ==  
	"""
	factors = factorize(n)
	total = 1
	for p,k in factors:
		total *= (p-1) * (p ** (k-1))
	return total

	# coeff = reduce(lambda x,y: x*(y[0]-1),factors, 1)
	# prod = reduce(lambda x,y: x*(y[1]))

def p72_factor():
	return sum(phi_factors(n) for n in xrange(2,N))

# print p72_factor()



