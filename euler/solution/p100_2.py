
from math import sqrt

inv_sq2 = 1./sqrt(2)

N = 10**12

while True:
	N += 1
	x = int(N * inv_sq2) + 1
	y = N - x
	if x**2 - x - 2*x*y - y**2 + y == 0:
		print x,y,N
		break
	if N % 10000000 == 0:
		print '\t',N

############################## (must get to 7000 --> ~ 4 days)

# k = 2*(10**12) + 5
k = 1999999999999
while True:
	k += 2   # k2 is 1 mod 4  (it is n*2 -1)
	k2 = k**2 # k2 is 1 mod 4
	v = 2*(k2+1)
	sqrtv = int(sqrt(v))
	if sqrtv**2 == v and v % 4 == 0 and v % 8 != 0:
		x = (sqrtv +2)/ 4
		y = int(0.5*(sqrt(8*(x**2)-8*x+1) - 2*x +1))
		N = x + y
		print k,v,x,y,N
		break
	if k % 10000001 == 0:
		print k
		break

# must get to 2140758220993 --> ACTUALLY NO FASTER....


# LB = 2000000000000

# ks = [ k**2 for k in xrange(LB,LB+200000000000) if k %2 == 1]  # x = 1/4 * ( sqrt(2(k+1)) + 2 )
# vs = [ 2*(k+1) for k in ks]
# xs = [ (int(sqrt(v)) + 2) / 4 for v in vs if is_good_v(v)]
# ys = [yfromx(x) for x in xs]
# print [ x + y for x,y in zip(xs,ys)]