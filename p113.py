
# 75 mins
# In [97]: %time %run p113.py
# 51161058134250
# CPU times: user 4.55 ms, sys: 1.86 ms, total: 6.4 ms
# Wall time: 6.1 ms

n = 10
def f(k):
	numer = reduce(lambda x,y: x*y, xrange(10,10+k),1)
	denom = reduce(lambda x,y: x*y, xrange(1,k+1),1)
	return numer/denom

def decf(k):
	return sum(f(k) for k in xrange(1,k+1)) - (k-1)

def nonbouncy(k):
	return f(k) + decf(k) - (k-1)*(9) - 10 - 1 # the extra minus one is becuase we don't count 0


def is_increasing(n):
	str_n = str(n)
	return all( int(a) <= int(b) for a,b in zip(str_n,str_n[1:]))

def is_decreasing(n):
	str_n = str(n)
	return all( int(a) >= int(b) for a,b in zip(str_n,str_n[1:]))

def is_bouncy(n):
	return not (is_increasing(n) or is_decreasing(n))


# def incr_ratio_ltn(n):

# def decr_ratio_ltn(n):

# def bouncy_ratio_ltn(n):
# 	bouncy = len(filter(is_bouncy,xrange(1,n+1)))
# 	return (bouncy,n - bouncy)

def categories_ltn(n):
	incr = len(filter(is_increasing,xrange(n)))
	decr = len(filter(is_decreasing,xrange(n)))
	bouncy = len(filter(is_bouncy,xrange(n)))
	nonbouncy = n - bouncy
	return (incr,decr,nonbouncy,bouncy)


print nonbouncy(100)
#incr NOT == decr!?!!?