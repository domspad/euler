

# 100 mins
# In [94]: %time %run p91.py
# 14234
# CPU times: user 11min 49s, sys: 3.98 s, total: 11min 53s
# Wall time: 12min 5s

# USE LINE PROF TO SEE WHY mp.almosteq SO SLOW

# In [5]: len(list(product(xrange(51),xrange(51),xrange(51),xrange(51))))
# Out[5]: 6765201

from itertools import starmap

import mpmath as mp


def are_perp(m1,m2):
	"""
	slopes are perpendicular
	
	m1,m2 in (-inf,inf)
	"""
	if m2 == 0:
		return m1 == float('inf') or m1 == -float('inf')
	else:
		return mp.almosteq(m1,-1./m2)  # THE CHANGE TO 

def slope(a,b):
	"""
	slope from a = (x1,y1) to b = (x2,y2) distinct points
	if vertical return float('inf') VALID PYTHON
	"""
	x1,y1 = a
	x2,y2 = b
	if x1 == x2:
		return float('inf')
	else:
		return 1.*(y2-y1)/(x2-x1)

def is_right_tri(a,b):
	"""
	points a,b in (0,0)...(50,50) and c is (0,0), returns whether a,b,c forms right triangle
	"""
	c = (0,0)
	# check points not same
	if a == b or a == c or b == c:
		return False
	# check if origin is right angle
	if (a[1] == 0 and b[0] == 0) or (b[1] == 0 and a[0] == 0):
		return True
	m1,m2,m3 = starmap(slope,((a,b),(b,c),(a,c)))
	# check if any slopes are perp (then it is right tri!)
	if any(starmap(are_perp,((m1,m2),(m1,m3)))):
		return True
	return False
	# check right tri using slopes
		# special case for vertical line

from itertools import product

# for x1,y1,x2,y2 in product(xrange(6),xrange(6),xrange(6),xrange(6)):
# 	if is_right_tri((x1,y1),(x2,y2)):
# 		print x1,y1,x2,y2

B = 51	# B == 15 is first time it is wrong! (917 != 920)
		# SLOWER WITH mp.almosteq
		# now from B = 5 --> 58ms, the time for 2*B is 20*time(B)
c = 0
for x1,y1,x2,y2 in product(xrange(B),xrange(B),xrange(B),xrange(B)):
	if is_right_tri((x1,y1),(x2,y2)):
		c += 1
print c/2


# DEBUGGING....
# from sympy.geometry import Triangle

# for x1,y1,x2,y2 in product(xrange(B),xrange(B),xrange(B),xrange(B)):
# 	a = (x1,y1)
# 	b = (x2,y2)
# 	c = (0,0)
# 	if a == b or a == c or b == c:
# 		continue
# 	tt = Triangle((0,0),(x1,y1),(x2,y2))
# 	if isinstance(tt, Triangle) and tt.is_right():
# 		if not is_right_tri((x1,y1),(x2,y2)):
# 			print (x1,y1),(x2,y2)


###
### THE BUGGGGG (FIX IS AT LINE 22 NOW USING mp.almosteq(m1,-1./m2))
### 
# In [68]: run p91.py (these are triangles I DID NOT CATCH)
# (3, 11) (14, 8)
# (4, 14) (9, 5)
# (8, 14) (11, 3)
# (9, 5) (4, 14)
# (11, 3) (8, 14)
# (14, 8) (3, 11)

# In [69]: is_right_tri((3,11),(14,8))
# Out[69]: False

# In [70]: Triangle((0,0),(3,11),(14,8))
# Out[70]: Triangle(Point(0, 0), Point(3, 11), Point(14, 8))

# In [71]: Triangle((0,0),(3,11),(14,8)).is_right()
# Out[71]: True

# In [72]: c = (0,0)

# In [73]: a = (3,11)

# In [74]: b = (14,8)

# In [75]: paste
# m1,m2,m3 = starmap(slope,((a,b),(b,c),(a,c)))

# ## -- End pasted text --

# In [76]: m1
# Out[76]: -0.2727272727272727

# In [77]: m2
# Out[77]: 0.5714285714285714

# In [78]: m3
# Out[78]: 3.6666666666666665

# In [79]: -1./m1
# Out[79]: 3.666666666666667

# In [80]: are_perp(m1,m3)
# Out[80]: False

# In [81]: m1 == -1./m3
# Out[81]: False
