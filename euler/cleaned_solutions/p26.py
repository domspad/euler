
#ROUGHLY 55 mins in!!! and no definite idea
# final idea: do long division!

# idea: num/den = 0.[head][rep][rep][rep]...
# 1 - generate arbitrary long sequence (so binary search until repeats)
# 2 - find head (longest non-repeating subseq)
# 3 - find repeating part


# decimal.getcontext().prec = int
# Decimal(1)/Decimal(7) = 0.<as-long-as-i-want>

# def decimal(num,den,N=100):
# 	"""
# 	give decimal representation of num/den up to 100 digits (or until 0)
# 	"""
# 	rep = []
# 	if num >= den:
# 		q = num/den
# 		num = num % den
# 		int_part = q
# 	# now num < den
# 	while num != 0:
# 		q, r = num/den, num%den
# 		rep.append(q)


# 	if int_part:
# 		return str(int_part) + '.' + ...
# 	else:
# 		return '0.' + ...

def repeat_length(num,den):
	"""
	assume num < den, returns length of repeating portion of num/den
	"""
	qrs = []
	while True:
		q,r = num/den, num%den
		num = r*10
		qrs.append((q,r))
		if r == 0: #non-repeating
			return 0
		idx = qrs.index((q,r))
		if idx != (len(qrs)-1): #found repeat
			return (len(qrs) - 1) - idx 


ll = [(i,repeat_length(1,i)) for i in xrange(2,1000)]
ll.sort(key=lambda x:x[1])


# decimal(1,3) = '0.' + '3'*98
# decimal(6,5) = '1.2'
# decimal(1,13) = '0.' + '076923'*16 + '07'