


# using pentagonal recurrence ~ 50mins
# In [1]: %time %run p78.py
# 55374
# CPU times: user 22.1 s, sys: 279 ms, total: 22.3 s
# Wall time: 23.3 s

PARTITIONS = [1,1,2]

def pent_idx_gen(n):
	"""
	return n-1,n-2,...n-p_i
	"""

	i = 1
	p_i = 1
	while p_i <= n:
		yield n-p_i
		p_i = ((-i)*(3*(-i)-1))/2
		if p_i > n:
			break
		yield n-p_i
		i += 1
		p_i = (i*(3*i-1))/2

# def p(n):
# 	return sum(((-1)**(k-1))*PARTITIONS[idx] for k,idx in enumerate(pent_idx_gen(n)))
from math import sqrt
def pp(n):
	if n < 0:
		return 0
	if n < len(PARTITIONS):
		return PARTITIONS[n]

	last_k = int((1/6.)*(sqrt((24*n + 1)) + 1)) + 1
	idxs = []
	for x in xrange(1,last_k+1):
		idxs.append(x)
		idxs.append(-x)
	return sum( int((-1)**(k-1)) * pp(n - k*(3*k - 1)/2) for k in idxs)  

### ^^^ WEIRD NOT RIGHT BEFORE I MADE (-1)**(k-1) an int?? LOOK INTO p(1000) e.g. 
# ALMOST WORKING BUT NOT AGREE FOR pp(1000) with 24,061,467,864,032,622,473,692,149,727,991 ????

def pp78():
	n = 3
	while True:
		next_p = pp(n)
		PARTITIONS.append(next_p)
		if next_p % 1000000 == 0:
			return n
		n += 1

print pp78()

# dp in 9 mins ... but it may be to slow (only fease for N < 10^5)


def p77():

	N = 10000
	COINS = xrange(1,N)

	dp_array = [ [0]*(N) for i in xrange(N)]

	for j in xrange(N):
		dp_array[0][j] = 1

	for i in xrange(1,N):
		for j in xrange(1,i+1):
			if j > i:
				break
			first_term = dp_array[i][j-1]
			second_term = dp_array[i-COINS[j-1]][j] if COINS[j-1] <= i else 0
			total = first_term + second_term
			dp_array[i][j] = total
		dp_array[i][i:] = [dp_array[i][i]]*(N-i)
		print i, dp_array[i][i] % 1000000
		if dp_array[i][-1] % 1000000 == 0:
			return i




