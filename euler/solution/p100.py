

# # 4:57
# In [108]: %time %run p100.py
# 756872327473
# CPU times: user 2.98 s, sys: 65.7 ms, total: 3.05 s
# Wall time: 3.1 s


# need to try Pell's equation solution...  https://oeis.org/A046090 and http://www.jpr2718.org/ax2p.pdf


# with sympy!
from sympy.abc import x,y
from sympy import simplify, symbols
from sympy.solvers.diophantine import diophantine
def p100():
	eq = x**2 - y**2 - 2*x*y - x + y
	n = symbols('n',integer=True)
	s = diophantine(eq,n)
	x_1,y_1 = s.pop()
	x_2,y_2 = s.pop()
	x_3,y_3 = s.pop()
	x_4,y_4 = s.pop()
	xxs = (x_1, x_2, x_3, x_4)
	yys = (y_1,y_2,y_3,y_4)
	print 'n eqnum x y '
	for i in xrange(9):
		for e,(xx,yy) in enumerate(zip(xxs,yys)):
			try:
				x_val = simplify(xx.subs({n:i}))
				if x_val > 0:
					y_val = simplify(yy.subs({n:i}))
					if x_val+y_val>10**12:
						print 'DONE', i, e, x_val, y_val, x_val+y_val, x_val+y_val>10**12
						return x_val
					print i, e, x_val, y_val, x_val+y_val, x_val+y_val>10**12
			except KeyError:
				print 'strange sympy error', i, e
print p100()


#BLAHHHHHHH
#REST###

	# from math import sqrt

	# m = 120
	# n = 85
	# b = n
	# r = m-b

	# frac = sqrt(1/2.0)

	# def ineqs(m=m,n=n):
	# 	return (n/float(m) - frac, frac - (n-1)/float(m-1))
	# 	# return (2*n > sqrt(2)*m ) (2*(n-1) < sqrt(2) *(m-1))

	# def parts(n):
	# 	return [(i,n-i) for i in xrange(1,n)
	# 					if float(i) / n > frac
	# 					if float(i-1) / (n-1) < frac]

	# # for b,r in sum([parts(n) for n in xrange(121)],[]):
	# #     print '\t'.join(map(str,[b,r,eqs(b,r)]))


	# LIM = 10**12
	# B = int(LIM / sqrt(2)) + 1


	# def p_eq(b):
	# 	return sqrt(8*(b-1)*b + 1)

	# def sq_sol(k):
	# 	"""
	# 	Returns true if (k^2+2) is an even square
	# 	"""
	# 	y = sqrt(2*(k**2) + 2)
	# 	return int(y) == y

	# # brute
	# # ~2 hrs before went to this solution
	# # ANS

	# #all less than 4,500,000,000: at ~ 2 sec per million (grows with number size)
	# 							   # ~ 5 sec per million once we hit 1 trillion!
	# 							   	# at 70 billiion...
	# # 4
	# # 21
	# # 120
	# # 697
	# # 4060
	# # 23661
	# # 137904
	# # 803761
	# # 4684660
	# # 27304197
	# # 159140520
	# # 927538921

	# def eqs(b=b,r=r):
	# 	return b**2 - b - 2*b*r - r**2 +r

	# # 	~5 sec per million! --> 70 bill ~ 350,000 secs! --> 4 days
	#  			# 5.554500103 			1030001000000
	# 			# 5.46113204956 			1030002000000
	# 			# 5.2989628315 			1030003000000
	# 			# 5.3919968605 			1030004000000

	# def check(m):
	# 	b = int(m / sqrt(2)) + 1
	# 	r = m - b
	# 	return b**2 - b - 2*b*r - r**2 +r == 0

	# from time import time
	# def p100():
	# 	"""
	# 	Start checking solutions starting from m = 1 trillion, return the first valid m
	# 	"""
	# 	st = time()
	# 	m = 10 ** 12
	# 	while True:
	# 		if check(m):
	# 			return m
	# 		if m % 1000000 == 0:
	# 			print '\t\t\t', time() - st, '\t\t\t',m
	# 			st = time()
	# 		m += 1

	# p100()


	# def xfromk(k):
	# 	v = 2*(k+1)
	# 	if is_square(v) and v % 4 == 0 and v % 8 != 0:
	# 		sq_v = int(sqrt(v))
	# 		sq_v += 2
	# 		return sq_v / 4
	# 	else:
	# 		return None

	# from math import sqrt 

	# def is_good_v(v):
	# 	return int(sqrt(v))**2 == v and v % 4 == 0 and v % 8 != 0



	# def yfromx(x):
	# 	return int(0.5*(sqrt(8*(x**2)-8*x+1) - 2*x +1))

	# ks = [ k**2 for k in xrange(2,100000) if k %2 == 1]  # x = 1/4 * ( sqrt(2(k+1)) + 2 )
	# vs = [ 2*(k+1) for k in ks]
	# xs = [ (int(sqrt(v)) + 2) / 4 for v in vs if is_good_v(v)]
	# ys = [yfromx(x) for x in xs]
	# ns = [ x + y for x,y in zip(xs,ys)]

	# # estimate ~ 1 day...`


	# def ns_uptok(K):
	# 	ks = [ k**2 for k in xrange(2,K) if k %2 == 1]  # x = 1/4 * ( sqrt(2(k+1)) + 2 )
	# 	vs = [ 2*(k+1) for k in ks]
	# 	xs = [ (int(sqrt(v)) + 2) / 4 for v in vs if is_good_v(v)]
	# 	ys = [yfromx(x) for x in xs]
	# 	return [ x + y for x,y in zip(xs,ys)]




	# # GENERAL DIOPHANTINE OF 2 variables 2nd powers solver?
	# #https://www.alpertron.com.ar/JQUAD.HTM
	# p,q,k,r,s,l = 5,2,-2,2,1,-1
	# # p,q,k,r,s,l = -1,2,1,2,-5,-1
	# x,y = 15,6
	# print x,y, x+y
	# for i in xrange(10):
	# 	x = p*x + q*y + k
	# 	y = r*x + s*y + l	
	# 	print x,y, x+y
	# #NOPE!

# BLAHHHH MORE

	# from math import sqrt

	# inv_sq2 = 1./sqrt(2)

	# N = 10**12

	# while True:
	# 	N += 1
	# 	x = int(N * inv_sq2) + 1
	# 	y = N - x
	# 	if x**2 - x - 2*x*y - y**2 + y == 0:
	# 		print x,y,N
	# 		break
	# 	if N % 10000000 == 0:
	# 		print '\t',N

	# ############################## (must get to 7000 --> ~ 4 days)

	# # k = 2*(10**12) + 5
	# k = 1999999999999
	# while True:
	# 	k += 2   # k2 is 1 mod 4  (it is n*2 -1)
	# 	k2 = k**2 # k2 is 1 mod 4
	# 	v = 2*(k2+1)
	# 	sqrtv = int(sqrt(v))
	# 	if sqrtv**2 == v and v % 4 == 0 and v % 8 != 0:
	# 		x = (sqrtv +2)/ 4
	# 		y = int(0.5*(sqrt(8*(x**2)-8*x+1) - 2*x +1))
	# 		N = x + y
	# 		print k,v,x,y,N
	# 		break
	# 	if k % 10000001 == 0:
	# 		print k
	# 		break

	# # must get to 2140758220993 --> ACTUALLY NO FASTER....


	# # LB = 2000000000000

	# # ks = [ k**2 for k in xrange(LB,LB+200000000000) if k %2 == 1]  # x = 1/4 * ( sqrt(2(k+1)) + 2 )
	# # vs = [ 2*(k+1) for k in ks]
	# # xs = [ (int(sqrt(v)) + 2) / 4 for v in vs if is_good_v(v)]
	# # ys = [yfromx(x) for x in xs]
	# # print [ x + y for x,y in zip(xs,ys)]