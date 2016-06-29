

# Brute force
# 8 mins to realize its fastest, and design
# +4 mins to code

# In [13]: %time p40()
# 210
# CPU times: user 236 ms, sys: 28.5 ms, total: 265 ms
# Wall time: 272 ms

def p40():
	digit_string = ''.join(map(str,range(1000000)))

	ns = [ 1, 10, 100, 1000, 10000, 100000, 1000000 ]

	total = 1

	for n in ns:
		total *= int(digit_string[n])

	print total


##############################################################

# plus 20 mins to find elegant functional solution...

def len_champernowne(m):
	"""
	Return the number of digits in Champernowne's constant up to the positive integer m (including)
	m int > 0
	"""
	num_digits = len(str(m))
	total = 0

	for i in xrange(num_digits - 1):
		total += (i + 1) * (9 * (10 ** (i)))

	# for last digit...
	total += (m - (10 ** (num_digits-1)) + 1) * num_digits

	return total

for i in xrange(1, 11):
	nd = int('9'*i)
	nd_prev = int(str(nd)[:-1] if nd > 9 else '0')
	t = len_champernowne(nd) - len_champernowne(nd_prev)
	print "{}\t{}".format(i, t)

1	9
2	180
3	2700
4	36000
5	450000
6	5400000
7	63000000
8	720000000
9	8100000000
10	90000000000

def nth_digit(n):
	"""
	Return the nth digit of Champernowne's constant.
	n int > 0
	"""
	pass

def slice_mult(slice):
	"""
	Return the product of the digits whose indices are in slice, of Champernowne's constant.
	slice : list of ints > 0

		e.g. slice_mult([ 1, 10, 100, 1000, 10000, 100000, 1000000 ]) == 210
	"""
