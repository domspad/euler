
from math import sqrt

m = 120
n = 85
b = n
r = m-b

frac = sqrt(1/2.0)

def ineqs(m=m,n=n):
	return (n/float(m) - frac, frac - (n-1)/float(m-1))
	# return (2*n > sqrt(2)*m ) (2*(n-1) < sqrt(2) *(m-1))

def parts(n):
	return [(i,n-i) for i in xrange(1,n)
					if float(i) / n > frac
					if float(i-1) / (n-1) < frac]

# for b,r in sum([parts(n) for n in xrange(121)],[]):
#     print '\t'.join(map(str,[b,r,eqs(b,r)]))


LIM = 10**12
B = int(LIM / sqrt(2)) + 1


def p_eq(b):
	return sqrt(8*(b-1)*b + 1)

def sq_sol(k):
	"""
	Returns true if (k^2+2) is an even square
	"""
	y = sqrt(2*(k**2) + 2)
	return int(y) == y

# brute
# ~2 hrs before went to this solution
# ANS

#all less than 4,500,000,000: at ~ 2 sec per million (grows with number size)
							   # ~ 5 sec per million once we hit 1 trillion!
							   	# at 70 billiion...
# 4
# 21
# 120
# 697
# 4060
# 23661
# 137904
# 803761
# 4684660
# 27304197
# 159140520
# 927538921

# def eqs(b=b,r=r):
# 	return b**2 - b - 2*b*r - r**2 +r

# 	~5 sec per million! --> 70 bill ~ 350,000 secs! --> 4 days
 			# 5.554500103 			1030001000000
			# 5.46113204956 			1030002000000
			# 5.2989628315 			1030003000000
			# 5.3919968605 			1030004000000

def check(m):
	b = int(m / sqrt(2)) + 1
	r = m - b
	return b**2 - b - 2*b*r - r**2 +r == 0

from time import time
def p100():
	"""
	Start checking solutions starting from m = 1 trillion, return the first valid m
	"""
	st = time()
	m = 10 ** 12
	while True:
		if check(m):
			return m
		if m % 1000000 == 0:
			print '\t\t\t', time() - st, '\t\t\t',m
			st = time()
		m += 1

