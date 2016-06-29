

# 1 hr into problem
# determined #points, and # of 3 sets
# trying to determine # of 3 sets of collinear points (i.e. NON triangles...)
	# via using coordinates and calculating collinearity...
	# BAD because not all 3 set points has lines between them

# 2.5 hrs into problem
# determined #lines and solution idea
	# all triangles are determined by 3 line segments (1 to 1)
	# check all line 3 sets of line segments

##### NEEDS NUMPY.....

# 5.75 hrs into problem
# SOLVED for N = 1... STILL problems with N=2 missing triangles!(counts == 88 but should be 104)
# how to iteratively generate all cuts
# debugged segment intersection 
# debugged measurement of triangle
# lines don't still intersect right
	
	# CPU times: user 30min 23s, sys: 5.38 s, total: 30min 29s
	# Wall time: 30min 36s

	# In [2]: counts
	# Out[2]: 259770

from math import sqrt
import numpy as np
from itertools import combinations

sq3 = sqrt(3)

A = np.array((0.,0.))
B = np.array((0.5, sq3/2.))
C = np.array((1., 0.))

AB = np.array((A,B))
BC = np.array((B,C))
AC = np.array((A,C))

bases = [AB,BC,AC]


# def add(P,Q):
# 	x1,y1 = P
# 	x2,y2 = Q
# 	return (x1 + x2, y1 + y2)

# def scale(P,w):
# 	"""
# 	scale P by w
# 	"""
# 	return tuple(map(lambda x: x*w, P))


# def avg(P,Q):
# 	"""
# 	Return avg of two points P, Q
# 	"""
# 	return scale(add(P,Q),0.5) 

def is_on(p,PQ):
	"""
	return True if p lies on segment PQ
	"""
	x,y = p
	x1,y1 = PQ[0]
	x2,y2 = PQ[1]
	if x >= min(x1,x2) and x <= max(x1,x2) and y >= min(y1,y2) and y <= max(y1,y2):
		return np.isclose((y2-y1)*(x-x2) - (x2-x1)*(y-y2),0)
	else:
		return False

def are_parallel(ab,cd):
	"""
	Return ab, cd are parallel (well-formed line segments)
	"""
	x1,y1 = ab[0]
	x2,y2 = ab[1]
	v1,w1 = cd[0]
	v2,w2 = cd[1]

	if x2 == x1:
		if v2 == v1:
			return True
		return False
	if v2 == v1:
		return False
		 
	return np.isclose((y2-y1)/(x2-x1),(w2-w1)/(v2-v1))

def intersect(ab,cd):
	"""
	Return coordinates of intersection of two segments (or None)
	"""
	x1,y1 = ab[0]
	x2,y2 = ab[1]
	v1,w1 = cd[0]
	v2,w2 = cd[1]

	# case 0 - return none if they are same
	if np.all(ab == cd):
		return None

	# case 1 - an endpoint of one seg is on the other
	for p, xy in [(ab[0],cd),(ab[1],cd),(cd[0],ab),(cd[1],ab)]:
		if is_on(p,xy):
			return p

	#case 2 - they intersect in middles
	A = np.array([[-1*(y2-y1), x2-x1],
					[-1*(w2-w1), v2-v1]])
	B = np.array([-1*(y2-y1)*x2 + (x2-x1)*y2,
				  (-1*(w2-w1)*v2 + (v2-v1)*w2)])
	try:
		Ainv = np.linalg.inv(A)
	except np.linalg.LinAlgError as e:
		if are_parallel(ab,cd):
			print "parallel"
		else:
		# print "Singular!"
			print ab[0], ab[1]
			print cd[0], cd[1]
			print '\n'
		return None
	xy = Ainv.dot(B)
	x,y = xy
	# check if lies on both segments
	if x >= min(x1,x2) and x <= max(x1,x2) and y >= min(y1,y2) and y <= max(y1,y2) \
	   and x >= min(v1,v2) and x <= max(v1,v2) and y >= min(w1,w2) and y <= max(w1,w2):
	   return xy
	else:
		return None

assert(intersect(AB,AB) == None)
Ac = AC.copy()
Ac[0][0] = 0.1
assert(intersect(AB,Ac) == None)
np.testing.assert_array_equal(intersect(AB,BC), np.array((0.5,sq3/2.)))

def filter_equals(pts):
	"""
	return list with dup arrays filtered
	"""
	k = len(pts)
	drops = [0]*k
	for i in xrange(k):
		for j in xrange(i+1,k):
			if np.allclose(pts[i],pts[j]):
				drops[j] = 1
	return [pts[i] for i in xrange(k) if drops[i] != 1]

def midpoint(A,B,w):
	"""
	Return w-scaled midpoint of AB
	"""
	return A + w*(B - A)

# def p163():
	
N = 2
A = np.array((0.,0.))
B = np.array((0.5, sq3/2.))
C = np.array((1., 0.))

AB = np.array((A,B))
BC = np.array((B,C))
AC = np.array((A,C))

# step 0 - Bases
bases = [AB,BC,AC]

# step 1 - cutters
cuts = []

for k in xrange(2*N + 1):
	w = 1. * k / (2*N)
	
	P1 = midpoint(A,C,w)
	P2 = np.array((P1[0],1))
	cuts.append((P1,P2))
	# cuts.append(np.array(P,))
	# P1 = scale(add(A,C), w)
	# P2 = 
	# cuts.append(np.array((P,(P[0],1)))  #vert cuts

	P1 = midpoint(A,B,w)
	P2 = P1 + np.array((sq3,-1))
	# P = scale(add(A,B), w)
	# direction = (sq3,-1)
	cuts.append((P1, P2))        # down right 30 cuts

	P1 = midpoint(B,C,w)
	P2 = P1 + np.array((-1 * sq3, -1))
	cuts.append((P1,P2))
	# P = scale(add(B,C), w)
	# direction = (-1 * sq3, -1)
	# cuts.append((P, add(P, direction))) 		# down left 30 cuts

for k in xrange(N+1):
	w = 1. * k / N
	
	d = np.array((0,sq3/2.))
	wd = w * d
	cuts.append((AC[0] + wd, AC[1] + wd))

	d = np.array((3./4,-sq3/4.))
	wd = w*d
	cuts.append((AB[0] + wd, AB[1] + wd))

	d = np.array((-3/4.,-sq3/4.))
	wd = w*d
	cuts.append((BC[0] + wd, BC[1] + wd))

print(len(cuts))

#step 2 - segments
segments = []
for cut in cuts:

	intersections = filter(lambda s: s is not None, [intersect(cut,b) for b in bases])
	pts = filter_equals(intersections)
	

	# pts = set(map(lambda s: tuple(s.tolist()),filter(lambda s: s is not None, [intersect(cut,b) for b in bases])))
	# pts = [np.array(s) for s in pts]

	if len(pts) != 2:
		pass
		# print pts, '\t\t\t',cut
	else:
		segments.append(np.array(pts))

counts = 0
tris = []
for segs in combinations(segments,3):
	s1,s2,s3 = segs
	i1, i2, i3 = intersect(s1,s2), intersect(s2,s3), intersect(s3,s1) 
	if i1 is not None and i2 is not None and i3 is not None:
		if np.all(i1 == i2) or np.all(i2 == i3) or np.all(i1 == i3):
			continue
		tris.append(np.array((intersect(s1,s2),intersect(s2,s3),intersect(s1,s3) )))
		counts += 1

print counts


# FOR LINE ADJUSTMENT

# import pylab as pl
# from matplotlib import collections  as mc

# lines = segments #+ [(np.array((0,0)),np.array((sq3,1)))]
# c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

# lc = mc.LineCollection(lines, linewidths=2)
# fig, ax = pl.subplots()
# ax.add_collection(lc)
# ax.autoscale()
# ax.set_xlim(-1,2)
# ax.set_ylim(-1,2)
# ax.margins(0.1)

# FOR POLYGONS!
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

from matplotlib import collections  as mc

lines = segments 

fig, ax = plt.subplots()
patches = []

for p in tris:
    polygon = Polygon(p, True)
    patches.append(polygon)

p = PatchCollection(patches, alpha=0.05)


ax.add_collection(p)


c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

lc = mc.LineCollection(lines, linewidths=2)
ax.add_collection(lc)


plt.show()
