
# 27 mins
# infer for m == 4, realized pattern, guessed formula for m == 50, found first n such that num_sols(n, 50) is > 1million
# In [30]: %time %run p115.py
# 168 1053389
# CPU times: user 2.01 ms, sys: 1 ms, total: 3.01 ms
# Wall time: 2.33 ms



def create_valid(m):
	"""
	create valid checker for min red block length == m
	"""
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
				if binary_rep[idx:idx+m] == (1,)*m: 
					#move to next change in color
					while idx < size and binary_rep[idx] == 1:
						idx += 1
				else:
					return False
			else:
				idx += 1
		return True

	return valid

from itertools import product 	

def binary_rep_gen(N):
	for binary_rep in product( *(xrange(2) for i in xrange(N))):
		yield binary_rep

# roughly doubles with each 1
def num_sols(N,m):
	valid = create_valid(m)
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
		seq = differences(seq)

# brute force calc ---> ~20 secons for up to 24, doubles for each additional, so up to 50 would be a while...
# vals = [num_sols(N) for N in xrange(1,25)]
# all_differences(vals)


def recursive_upto_n(n):
	"""
	n >= 51
	starting with formula
		a_n = 2*a_n-1 - a_n-2 + a_n-51
		a_1 = 1
		a_2 = 1	
		...
		a_49 = 1
		a_50 = 2
		a_51 = 4
	"""
	starting = [1]*49 + [2,4]
	idx = 51
	while idx < n:
		a,b,c = starting[-1], starting[-2], starting[-51]
		starting.append(2*a - b + c)
		idx += 1
	return starting

seq = recursive_upto_n(200)
print 168, seq[167]