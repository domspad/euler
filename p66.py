
#25 mins brute force code --- probably AWHILE for all D<=1000 :(
	# and analysis of hard cases (can get ~600 cases < 1000 with brute)


from math import sqrt
from time import time
def is_square(n):
	return int(sqrt(n))**2 == n

def brute_min_x(D, max_time=0.3):
	"""
	brute force solves x^2 - Dy^2 = 1,
	D NOT SQUARE
	"""
	start = time()
	x = 2
	xx = x**2
	while True and time() - start < max_time:
		# y = 1
		y = sqrt((xx - 1.)/D)  #SMART Y START // DONT EVEN NEED ITER ON Y!
		if float(int(y)) == y:
			return x
		# while xx - D*(y**2) > 1 :
		# 	# print xx, D*(y**2)
		# 	y += 1
		# if xx - D*(y**2) == 1:
		# 	return x
		x += 1
		xx = x**2
	print '\t', D


# print max( brute_min_x(D) for D in xrange(2,40) if not is_square(D))	
HARD = [] # 404 problems that require > 0.3 secs brute force

for D in xrange(100):
	if not is_square(D):
		ans = brute_min_x(D)
		if ans:
			print D, brute_min_x(D)
		else:
			HARD.append(D)