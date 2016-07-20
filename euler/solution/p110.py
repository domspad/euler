
# this was an amalgamation of files and ad hoc attempts. The time I spent wasn't tracked but was
# probably on the order of 3 hours



from math import sqrt
from collections import defaultdict

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIMES = primes_lt3(10000)
	# Wall time: 11.7 s

def prime_fact_upto(n):
	"""
	n > 1, return prime facts of all integers up to n

	12 --> {2:2, 3:1}
	"""
	PRIME_FACTS = [defaultdict(int),defaultdict(int)]
	for i in xrange(2,n):
		if i in PRIMES:
			new_pf = defaultdict(int)
			new_pf[i] = 1
			PRIME_FACTS.append(new_pf)
		else:
			for p in PRIMES:
				if p > sqrt(i) + 1: # not one found!
					new_pf = defaultdict(int)
					new_pf[i] = 1
					PRIME_FACTS.append(new_pf)
					break
				elif i % p == 0:
					new_pf = PRIME_FACTS[i/p].copy()
					new_pf[p] += 1
					PRIME_FACTS.append(new_pf)
					break
	return PRIME_FACTS

PRIME_FACTS = prime_fact_upto(100)
	# Wall time: 25min 7s

def fact_to_num(fact):
	total = 1
	for k,v in fact.iteritems():
		total *= k**v
	return total

def fact_to_exp_rep(fact):
	tup_len = max(PRIMES.index(p) for p in fact.keys()) if len(fact) > 0 else 0
	rep = [0]*(tup_len+1)
	for k,v in fact.iteritems():
		rep[PRIMES.index(k)] = v
	return tuple(rep)

def fact_to_prime_rep(fact):
	rep = []
	for k,v in fact.iteritems():
		rep.extend([k]*v)
	return tuple(rep)


def y_given_x(x,n):
	flx = float(x)
	return (n*flx)/(flx - n)

def is_int(f):
	return float(int(f)) == f

def num_sols(n):
	c = 0
	for x in xrange(n+1, (2*n) + 1):
		y = y_given_x(x,n)
		if is_int(y):
			c += 1
			# print '\t',x,y
	# print '\t', c
	return c 

enum_prime_facts = list(enumerate(prime_fact_upto(100)))
enum_prime_facts.pop(0)
new_epfs = [epf + (fact_to_exp_rep(epf[1]),) + (fact_to_prime_rep(epf[1]),) + (num_sols(epf[0]),) for epf in enum_prime_facts]

datas = [[epf[-1] for epf in  sorted(new_epfs,key=lambda epf: epf[idx])] for idx in (0,1,2,3)]

import pandas as pd 
import matplotlib.pyplot as plt 

xs = range(99)
for ys in datas:
	fig, ax = plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
	ser = pd.Series(data=ys, index=xs)
	ser.plot(ax=ax,kind='line',title=None,logx=False,logy=False,loglog=True)
		# - 'line' : line plot (default)
	#     - 'bar' : vertical bar plot
	#     - 'barh' : horizontal bar plot
	#     - 'hist' : histogram
	#     - 'box' : boxplot
	#     - 'kde' : Kernel Density Estimation plot
	#     - 'density' : same as 'kde'
	#     - 'area' : area plot
	#     - 'pie' : pie plot
	plt.show()



#############################################################################
#############################################################################
# Smarter int generator



from math import sqrt
from collections import defaultdict

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIMES = primes_lt3(10000)


from Queue import deque

def get_value(rep):
	total = 1
	for a,p in zip(rep,PRIMES):
		total *= p**a
	return total

def get_children(rep):

	children = []
	if len(rep) == 1:
		children = [(1,0)]
	elif len(rep) == 2:
		children = [(rep[0]+1,0),(rep[0],1,0)]
	else:
		if rep[-2] == rep[-3]:
			children = [rep[:-1] + (1,0)]
		else:
			children = [rep[:-2] + (rep[-2]+1,0) ,rep[:-1] + (1,0)]
	return children

def growing_exps():
	fringe = deque([(0,)])
	while True:
		rep = fringe.popleft()

		# append children
		fringe.extend(get_children(rep))
		# yield val
		yield rep



### ADDED SPICE


from sympy import gcd, divisors

def are_coprime(pair):
	m,n = pair
	return gcd(m,n) == 1

def num_sols_gcd(n):
	divs = divisors(n)
	c = 0
	for e, d1 in enumerate(divs):
		for d2 in divs[e:]:
			if are_coprime((d1,d2)):
				c += 1
	return c

# ### HERE WE GO

# g = growing_exps()

# smallest_above_mil = 10**72
# smallest_val = 0

# for i in g:
# 	sols = num_sols_gcd(i)
# 	if sols > 1000 and i < smallest_above_mil:
# 		smallest_above_mil, smallest_val = i, sols
# 		break
#############################################################################
#############################################################################

ll = sorted([next(g) for i in xrange(10000)],key=exp_rep_to_num)

for il in ll:
	if exp_rep_to_weak_corpime(il) > 4*(10**6):
		print il, exp_rep_to_num(il)
    	break

#############################################################################
#############################################################################

from math import sqrt
from collections import defaultdict

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIMES = primes_lt3(10000)


from Queue import deque

def get_value(rep):
	total = 1
	for a,p in zip(rep,PRIMES):
		total *= p**a
	return total

def get_children(rep):

	children = []
	if len(rep) == 1:
		children = [((1,0),2)]
	elif len(rep) == 2:
		one = (rep[0]+1,0)
		two = (rep[0],1,0)
		children = [(one,get_value(one)),(two,get_value(two))]
	else:
		if rep[-2] == rep[-3]:
			one = rep[:-1] + (1,0)
			children = [(one,get_value(one))]
		else:
			one = rep[:-2] + (rep[-2]+1,0) 
			two = rep[:-1] + (1,0)
			children = [(one,get_value(one)) , (two, get_value(two))]
	return children

def growing_exps():
	fringe = deque([((0,),1)])
	while True:
		rep, val = fringe.popleft()

		# append children
		fringe.extend(get_children(rep))
		fringe = deque(sorted(fringe,key=lambda x:x[1]))
		# fringe.sort(key=lambda x:x[1])
		# yield val
		yield val



### ADDED SPICE


from sympy import gcd, divisors

def are_coprime(pair):
	m,n = pair
	return gcd(m,n) == 1

from itertools import combinations_with_replacement

def num_sols_gcd(n):
	divs = divisors(n)
	c = 0
	return len(filter(are_coprime,combinations_with_replacement(divs,2)))
	# for d1, d2 in combinations_with_replacement(divs,2):
	# 	if are_coprime((d1,d2)):
	# 		c += 1	
	# return c

### HERE WE GO

g = growing_exps()

smallest_above_mil = 10**72
smallest_val = 0

for i in g:
	sols = num_sols_gcd(i)
	if sols > 10000:
		smallest_above_mil, smallest_val = i, sols
		break


#################################################################




PRIMES = (2,3,5,7,11,13)

from itertools import product
def exp_rep_to_divs(exp_rep):
	"""
	(3,1,2) --> [(0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1), (2, 0, 0), (2, 0, 1)]
	"""
	return product(*(xrange(i+1) for i in exp_rep))


g = exp_rep_to_divs((3,1,0))


def exp_rep_to_num(exp_rep):
	num = 1
	for p,a in zip(PRIMES,exp_rep):
		num *= p**a
	return num

def exp_rep_to_num_coprime(exp_rep):
	"""
	6 = (1,1) has 1,6 and 2,3 as coprimereps
	== 2^(K-1)
	"""
	if all(x == 0 for x in exp_rep):
		return 1 
	return 2**(len(filter(lambda x: x>0,exp_rep))-1)

def exp_rep_to_weak_corpime(exp_rep):
	return sum(map(exp_rep_to_num_coprime, exp_rep_to_divs(exp_rep)))


exp_rep = (3,1,0) #24)

assert sorted(map(exp_rep_to_num, exp_rep_to_divs(exp_rep))) == [1, 2, 3, 4, 6, 8, 12, 24]


##########################################################################

# 608,500,527,054,420 
# In [19]: %time num_sols_gcd(2*reduce(lambda x,y: x*y, PRIMES[:13], 1))
# CPU times: user 6h 22min 18s, sys: 1min 15s, total: 6h 23min 33s
# Wall time: 1d 5h 11min 43s
# Out[19]: 1328603


# 85 mins
# running time? estimate...

from math import sqrt
from collections import defaultdict

def primes_lt3(N):
	"""
	Return all primes less than N > 0 int
	"""
	# test every number less than N/2
	primes = [ i for i in xrange(2,N)
				 if not any( ( i % p == 0 for p in xrange(2,int(sqrt(i))+1) ) )]

	return primes

PRIMES = primes_lt3(10000)
	# Wall time: 11.7 s

def prime_fact_upto(n):
	"""
	n > 1, return prime facts of all integers up to n

	12 --> {2:2, 3:1}
	"""
	PRIME_FACTS = [defaultdict(int),defaultdict(int)]
	for i in xrange(2,n):
		if i in PRIMES:
			new_pf = defaultdict(int)
			new_pf[i] = 1
			PRIME_FACTS.append(new_pf)
		else:
			for p in PRIMES:
				if p > sqrt(i) + 1: # not one found!
					new_pf = defaultdict(int)
					new_pf[i] = 1
					PRIME_FACTS.append(new_pf)
					break
				elif i % p == 0:
					new_pf = PRIME_FACTS[i/p].copy()
					new_pf[p] += 1
					PRIME_FACTS.append(new_pf)
					break
	return PRIME_FACTS

PRIME_FACTS = prime_fact_upto(10000)
	# Wall time: 25min 7s

from itertools import product, ifilter

def pf_to_divs(pf):
	"""
	give all proper divisors, given a prime factorization
	{p:num, 2:2, 3:4} --> []
	"""
	items = pf.items()
													# QUESTION is order of iter from dict ALWAYS the same?
	iter_exp = product(*(xrange(a+1) for _,a in items))
	divs = []
	for exp in iter_exp:
		total = 1
		for i, a in enumerate(exp):
			total *= items[i][0]**a
		divs.append(total)
	#pop last total because it is not proper
	divs.pop()
	return divs

from sympy import gcd, divisors

def are_coprime(pair):
	m,n = pair
	return gcd(m,n) == 1

def num_sols_gcd(n):
	divs = divisors(n)
	c = 0
	for e, d1 in enumerate(divs):
		for d2 in divs[e:]:
			if are_coprime((d1,d2)):
				c += 1
	return c

# coprimes = set([(1,1)])
# divs = pf_to_divs(PRIME_FACTS[2*2*3*3*5])

# filter(are_coprime, product(divs,divs))


		