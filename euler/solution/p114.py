# -*- coding: utf-8 -*-

# 96 mins
# 60 mins trying to smart brute force it...
# +36 minutes discovering recursive relation with difference equations
# In [56]: %time %run p114.py
# 16475640049
# CPU times: user 2.26 ms, sys: 884 µs, total: 3.15 ms
# Wall time: 2.66 ms





def valid(binary_rep):
	"""
	(1,1,1,0) --> True
	(1,1,0) --> False

	req binary_rep len at least 1
	"""
	idx = 0
	size = len(binary_rep)
	while idx < size: #all UP TO idx is valid (excluding idx)...
		if binary_rep[idx] == 1:
			#check at least 3 reds
			if binary_rep[idx:idx+3] == (1,1,1): 
				#move to next change in color
				while idx < size and binary_rep[idx] == 1:
					idx += 1
			else:
				return False
		else:
			idx += 1
	return True

from itertools import product

def binary_rep_gen(N):
	for binary_rep in product( *(xrange(2) for i in xrange(N))):
		yield binary_rep

# roughly doubles with each 1
def num_sols(N):
	return len(filter(valid,binary_rep_gen(N)))



def differences(seq):
	"""
	return difference sequence of seq
	[1,2,3,4] ---> [1,1,1]
	"""
	return map(lambda x: x[1] - x[0], zip(seq, seq[1:]))

def all_differences(seq):
	while len(seq) != 0:
		print seq, '\n'
		seq = differences(seq)[1:]

# brute force calc ---> ~20 secons for up to 24, doubles for each additional, so up to 50 would be a while...
# vals = [num_sols(N) for N in xrange(1,25)]
# all_differences(vals)


def recursive_upto_n(n):
	"""
	n >= 4
	starting with formula
		a_n = 2*a_n-1 - a_n-2 + a_n-4
		a_1 = 1
		a_2 = 1
		a_3 = 2
		a_4 = 4
	"""
	starting = [1,1,2,4]
	idx = 4
	while idx < n:
		a,b,c = starting[-1], starting[-2], starting[-4]
		starting.append(2*a - b + c)
		idx += 1
	return starting

print recursive_upto_n(50)[-1]