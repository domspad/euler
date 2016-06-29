

# 60 mins with knowledge of cont frac search
# In [62]: %time %run p66.py
# 661
# CPU times: user 1.29 s, sys: 20.2 ms, total: 1.31 s
# Wall time: 1.32 s
### realized this is Pell Equation!
### fund solution (that min x) has form of one of convergents for sq(D)
### AND faster way of calculating cont frac convergents via recursive solution
#https://en.wikipedia.org/wiki/Continued_fraction#Calculating_continued_fraction_representations

from math import sqrt

def close(a,b,rtol=1.e-5,atol=1.e-8):
	return abs(a - b) <= (atol + rtol*abs(b))

def is_square(n):
	return int(sqrt(n)) ** 2 == n



from math import floor
import mpmath as mp

# mp.dps = 1000  # DOESNT MATTER?

# FROM PROB 64.py
def cont_frac_expansion_sqrt(n):
	"""
	n is NOT square
	e.g. 2 --> (1,2) (2 repeats)
	"""
	if is_square(n):
		return 0
	seq = []
	r = mp.sqrt(n,prec=1000) # DOESNT MATTER?
	a = floor(r)
	fls = [r]
	seq.append(int(a))
	r = mp.fdiv(1.,mp.fsub(r,a,prec=1000),prec=1000)
	a = floor(r)
	fls.append(r)
	seq.append(int(a))
	r = mp.fdiv(1.,mp.fsub(r,a,prec=1000),prec=1000) #THESE TWO MATTER!!!
	a = floor(r)
	fls.append(r)
	seq.append(int(a))
	while not close(r, fls[1]):
		r = mp.fdiv(1.,mp.fsub(r,a,prec=1000),prec=1000) #THESE TWO MATTER!!!
		a = floor(r)
		fls.append(r)
		seq.append(int(a))
	# print seq
	seq.pop()
	return seq

def sqrt_as_gen(n):
	notation = cont_frac_expansion_sqrt(n)
	base, rest = notation[0],notation[1:]
	k = len(rest)
	yield base
	i = 0
	while True:
		yield rest[i % k]
		i += 1

def convergents_sqrt_gen(n):
	"""
	yield convergents of sqrt(n) 
	"""
	gg = sqrt_as_gen(n)
	a0 = next(gg)
	hs = [0,1,a0*1 + 0]
	ks = [1,0,a0*0 + 1]
	yield (hs[-1],ks[-1])
	while True:
		an = next(gg)
		hs = hs[1:] + [an*hs[-1] + hs[-2]]
		ks = ks[1:] + [an*ks[-1] + ks[-2]]
		yield (hs[-1],ks[-1])

def conv_min_x(D):
	"""
	D NOT square
	"""
	for (x,y) in convergents_sqrt_gen(D):
		if x**2 - (D*(y**2)) == 1:
			return x

print max(((D,conv_min_x(D)) for D in xrange(2,1001) if not is_square(D)), key=lambda x: x[1])[0]



########################################################################
#25 mins brute force code --- probably AWHILE for all D<=1000 :(
	# and analysis of hard cases (can get ~600 cases < 1000 with brute)


from math import sqrt
from time import time
def is_square(n):
	return int(sqrt(n))**2 == n

def brute_min_x(D, max_time=0.3):
	"""
	brute force solves x^2 - Dy^2 = 1,
	D NOT SQUARE
	"""
	start = time()
	x = 2
	xx = x**2
	while True and time() - start < max_time:
		# y = 1
		y = sqrt((xx - 1.)/D)  #SMART Y START // DONT EVEN NEED ITER ON Y!
		if float(int(y)) == y:
			return x
		# while xx - D*(y**2) > 1 :
		# 	# print xx, D*(y**2)
		# 	y += 1
		# if xx - D*(y**2) == 1:
		# 	return x
		x += 1
		xx = x**2
	print '\t', D


# print max( brute_min_x(D) for D in xrange(2,40) if not is_square(D))	
HARD = [] # 404 problems that require > 0.3 secs brute force

# for D in xrange(100):
# 	if not is_square(D):
# 		ans = brute_min_x(D)
# 		if ans:
# 			print D, brute_min_x(D)
# 		else:
# 			HARD.append(D)
