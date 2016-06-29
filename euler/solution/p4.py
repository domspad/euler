
# BRUTE! from start to finish 14 mins
# In [39]: %time p4()
# CPU times: user 513 ms, sys: 52.2 ms, total: 565 ms
# Wall time: 527 ms
# Out[39]: 906609



def is_palindrome(n):

	# reverse string and check equal
	n_str = str(n)
	rev_n_str = reversed(n_str)
	for i in xrange(len(n_str)):
		if n_str[i] != rev_n_str.next():
			return False
	return True


def p4():

	largest_palindrome = 0 
	for i in xrange(100, 1000):
		for j in xrange(i, 1000):   #dont need to test all pairs twice!
			n = i * j
			if is_palindrome(n) and n > largest_palindrome:
				largest_palindrome = n

	return largest_palindrome


