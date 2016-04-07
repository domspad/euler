
from math import sqrt

m = 120
n = 85
b = n
r = m-b

frac = sqrt(1/2.0)

def eqs(b=b,r=r):
	return b**2 - b - 2*b*r - r**2 +r

def ineqs(m=m,n=n):
	return (n/float(m) - frac, frac - (n-1)/float(m-1))
	# return (2*n > sqrt(2)*m ) (2*(n-1) < sqrt(2) *(m-1))

def parts(n):
	return [(i,n-i) for i in xrange(1,n)
					if float(i) / n > frac
					if float(i-1) / (n-1) < frac]

for b,r in sum([parts(n) for n in xrange(121)],[]):
    print '\t'.join(map(str,[b,r,eqs(b,r)]))