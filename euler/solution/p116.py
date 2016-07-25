
# reuse some from p115
# 30 mins
# In [49]: %time %run p116.py
# 20492570929
# CPU times: user 2.64 ms, sys: 4.76 ms, total: 7.4 ms
# Wall time: 9.57 ms



def create_valid(m):
	"""
	create valid checker for min block length == m
	no buffer between blocks necessary
	at least one block must be placed
	blocks come in a fixed size
	"""
	def valid(binary_rep):
		"""
		(1,1,1,0) --> True
		(1,1,0) --> False

		req binary_rep len at least 1
		"""
		idx = 0
		size = len(binary_rep)
		at_least_one_block = False
		while idx < size: #all UP TO idx is valid (excluding idx)...
			if binary_rep[idx] == 1:
				at_least_one_block = True
				#check some multiple of m colored blocks
				start = idx
				while idx < size and binary_rep[idx] == 1:
					idx += 1
				num = idx - start
				if num % m != 0:
					return False
			else:
				idx += 1
		return at_least_one_block

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


def red_recursive_upto_n(n):
	"""
	starting with formula
		a_n = 2*a_n-1 - a_n-3
		a_1 = 0
		a_2 = 1	
		a_3 = 2
	"""
	starting = [0,1,2]
	idx = 3
	while idx < n:
		a,b= starting[-1], starting[-3]
		starting.append(2*a - b)
		idx += 1
	return starting

def green_recursive_upto_n(n):
	"""
	starting with formula
		a_n = 2*a_n-1 - a_n-2 + a_n-3 - a_n-4
		a_1 = 0
		a_2 = 0
		a_3 = 1
		a_4 = 2
		a_5 = 3
	"""
	starting = [0,0,1,2,3]
	idx = 5
	while idx < n:
		a, b, c, d = starting[-1], starting[-2], starting[-3], starting[-4]
		starting.append(2*a - b + c - d)
		idx += 1
	return starting

def blue_recursive_upto_n(n):
	"""
	starting with formula
		a_n = 2*a_n-1 - a_n-2 + a_n-4 - a_n-5
		a_1 = 0
		a_2 = 0
		a_3 = 0
		a_4 = 1
		a_5 = 2
		a_6 = 3
	"""
	starting = [0,0,0,1,2,3]
	idx = 6
	while idx < n:
		a,b, c, d= starting[-1], starting[-2], starting[-4], starting[-5]
		starting.append(2*a - b + c -d)
		idx += 1
	return starting

print red_recursive_upto_n(50)[-1] + green_recursive_upto_n(50)[-1] + blue_recursive_upto_n(50)[-1]
