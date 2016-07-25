
# reuse some from p116
# 21 mins
# recognized recursive formula after doing some subtractions of the difference sequences... (harder)
# In [28]: %time %run p117.py
# 100808458960497
# CPU times: user 1.89 ms, sys: 2.18 ms, total: 4.07 ms
# Wall time: 11 ms


def valid(quarnary_rep):
	"""
	(1,1,1,0) --> True
	(1,1,0) --> False

	req quarnary_rep len at least 1
	"""
	idx = 0
	size = len(quarnary_rep)
	while idx < size: #all UP TO idx is valid (excluding idx)...
		if quarnary_rep[idx] == 1:
			#check some multiple of m colored blocks
			start = idx
			while idx < size and quarnary_rep[idx] == 1:
				idx += 1
			num = idx - start
			if num % 2 != 0:
				return False
		elif quarnary_rep[idx] == 2:
			#check some multiple of m colored blocks
			start = idx
			while idx < size and quarnary_rep[idx] == 2:
				idx += 1
			num = idx - start
			if num % 3 != 0:
				return False
		elif quarnary_rep[idx] == 3:
			#check some multiple of m colored blocks
			start = idx
			while idx < size and quarnary_rep[idx] == 3:
				idx += 1
			num = idx - start
			if num % 4 != 0:
				return False
		else:
			idx += 1
	return True


from itertools import product 	

def quarnary_rep_gen(N):
	for quarnary_rep in product( *(xrange(4) for i in xrange(N))):
		yield quarnary_rep

# roughly doubles with each 1
def num_sols(N):
	return len(filter(valid,quarnary_rep_gen(N)))

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
	starting with formula
		a_n = 2*a_n-1 - a_n-5
		a_1 = 1
		a_2 = 2
		a_3 = 4
		a_4 = 8
		a_5 = 15
	"""
	starting = [1,2,4,8,15]
	idx = 5
	while idx < n:
		a,b= starting[-1], starting[-5]
		starting.append(2*a - b)
		idx += 1
	return starting

print recursive_upto_n(50)[-1]
