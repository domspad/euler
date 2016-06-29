

#90 mins - better arb floating point arithmatic!
# In [67]: %time %run p64.py
# 1322
# CPU times: user 31.2 s, sys: 267 ms, total: 31.4 s
# Wall time: 31.8 s




from math import sqrt

def close(a,b,rtol=1.e-5,atol=1.e-8):
	return abs(a - b) <= (atol + rtol*abs(b))

def is_square(n):
	return int(sqrt(n)) ** 2 == n



from math import floor
import mpmath as mp

# mp.dps = 1000  # DOESNT MATTER?

def sq_period_rec(N):
	if is_square(N):
		return 0
	seq = []
	r = mp.sqrt(N,prec=1000) # DOESNT MATTER?
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
		fls.append(r)
		r = mp.fdiv(1.,mp.fsub(r,a,prec=1000),prec=1000) #THESE TWO MATTER!!!
		a = floor(r)
		fls.append(r)
		seq.append(int(a))
	# print seq
	return len(seq) - 2

print sum(1 for N in xrange(2,10001) if sq_period_rec(N) % 2 == 1)




#### OLDDDDD WRONGGG
	#50 mins to code -- fragile floating point comparison brute solution
	# In [48]: %time %run p64.py
	# 4166
	# CPU times: user 9min 56s, sys: 3.17 s, total: 10min
	# Wall time: 10min 6s

	#### FRAGILE AT 15 terms!!!

	# ex: sq_period(691) should == 38 BUT we got 22
		# p691 = [26, 3, 2, 17, 10, 2, 5, 2, 1, 2, 1, 4, 1, 1, 8, 4, 1, 1, 1, 25, 1, 1, 1, 4, 8, 1, 1, 4, 1, 2, 1, 2, 5, 2, 10, 17, 2, 3, 52]
def sq_period(N):
	"""
	Returns period of sqrt(N) cont frac expansion
	"""
	if is_square(N):
		return 0
	seq = []
	fls = []
	fl = sqrt(N)
	fls.append(fl)
	I = int(fl)
	seq.append(I)
	fl = 1. / (fl - I)
	while not any(close(fl,prev) for prev in fls):
		fls.append(fl)
		I = int(fl)
		seq.append(I)
		fl = 1. / (fl - I)
	# print seq, len(seq)
	return len(fls) -1#, seq


# NOT AFFECTED BY 'close'
# NOT AFFECTED BY 'Decimal'
# from math import floor
# from decimal import Decimal
# def sq_period_rec(N):
# 	if is_square(N):
# 		return 0
# 	seq = []
# 	r = Decimal(sqrt(N))
# 	a = floor(r)
# 	seq.append(int(a))
# 	for i in xrange(30):
# 		r = Decimal(1.)/(r - Decimal(a))
# 		a = floor(r)
# 		seq.append(int(a))
# 	return seq




# sqN = sqrt(N)
# I = int(sqN)
# F = (1, sqN - I) #frac (denom is remainder)

# seq = []
# seq.append(I)

# nI = int(F[0]/F[1])
# F = (F[1] + 2**I ,N - I**2)
# I = nI

# seq.append(I)

# nI = int(F[0]/F[1])
# seq.append(nI)



# # F = sqN - I

# conv = []
# conv.append((I,F))


# #UHOH!!!! - Floating point error
# # In [8]: 1/F 
# # Out[8]: 1.2565473604732462

# # In [9]: ((sqN + 4)/7)
# # Out[9]: 1.2565473604732456

