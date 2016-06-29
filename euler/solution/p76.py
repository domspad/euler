

# 75 minutes - brute forced (no memoization)
# In [1]: time %run p76.py
# 190569291
# CPU times: user 9min 1s, sys: 3.61 s, total: 9min 5s
# Wall time: 9min 24s

# 190569291 (NUMBER OF partitions of 100)
	# while True:
	# 	part = next_partition(part,N)
# 10*190569291=1905692910 guess at average length of partitions ~ 20 for 100  (so take half length)


class NoBoundary(Exception):
	pass

def find_boundary(part):
	"""
	if part = (1,1,1,..,1): throws error
	"""
	if part[-1] == 1:
		idx = part.index(1) - 1
		if idx == -1:
			raise NoBoundary
		else:
			return idx
	else:
		return len(part) - 1


def next_partition(part, N):
	"""
	(a1, a2, ..., ak)
	a1 >= a2 >= a3 ... >= ak > 0
	a1 + ... + ak = N
	"""
	try:
		idx = find_boundary(part)
	except NoBoundary:
		raise StopIteration

	start, end = tuple(part[:idx]), tuple(part[idx:])
	bound = part[idx] - 1
	
	start_sum = sum(start)
	remain_sum = N - start_sum
	q,r = divmod(remain_sum, bound)
	if r != 0:
		next_part = start + (bound,)*q + (r,)
	else:
		next_part = start + (bound,)*q 
	return next_part


def p76():
	N = 100
	c = 0
	part = (N,)
	try:
		while True:
			part = next_partition(part,N)
			c += 1
	except StopIteration:
		print c

p76()