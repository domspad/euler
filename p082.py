

# , still need solution for M X 3 case (already have M X 2 case, which is sort of like base case)
									# or even 2 X N case, which is more illustritave of "recursive" case
# can already characterize solution as R, ...., R (cannot start,end with up/downs)
					# but already have counter examples for many other algorithms I've tried

# 1 hr, 35 mins
# GOT IT ! The "OPTIMISTIC, but not complete" actually turned into a complete solution finder!
# In [23]: time %run p082.py
# 260324.0
# CPU times: user 2.92 s, sys: 25.4 ms, total: 2.94 s
# Wall time: 2.96 s


case_ans = {'p082_small.txt':4,
			'p082_small2.txt':4,
			'p082_big.txt':994}
			# 'p082_matrix.txt':


# optimism?
# keep track of running totals, and only ever hold on to the top (smallest) M^3 totals


import numpy as np

fname = 'p082_matrix.txt'
# read in matrix
with open(fname, 'rb') as f:
	mat = np.loadtxt(f,delimiter=",").tolist()
	M = len(mat)
	N = len(mat[0])
# subtotals tracker
# [(subtotal, i, j)]
subtotals = [(mat[i][0],i,0) for i in xrange(M)]

# { (i,j): subtotal}
subtotals = {(i,0): mat[i][0] for i in xrange(M)}

# only need N-1 Rights to get all the way across
for step in xrange(N-1):
	# print sorted(subtotals.items(),key=lambda x: x[0])
	new_subtotals = {}
	for idxs,subtotal in subtotals.items():
		i,j = idxs
		for ii in xrange(M):
			# compute additional path from i,j to ii,j+1 via up/down then right
			new_subtotal = subtotal
			add = 0
			if i == ii:
				add = 0
				# skip
			elif i < ii:
				add = sum(mat[xi][j] for xi in xrange(i+1,ii+1)) #include ii_th but not i_th
			else: # i > ii
				add = sum(mat[xi][j] for xi in xrange(ii,i))	#include ii_th but not i_th
			add += mat[ii][j+1]

			new_subtotal += add
			# only append if better than best up to then or if the first up to then
			if (ii,j+1) in new_subtotals:
				if new_subtotals[(ii,j+1)] > new_subtotal:
					# print "replace appending, ", (i,j), ' to ', (ii,j+1), new_subtotal
					new_subtotals[(ii,j+1)] = new_subtotal
			else:
				# print "new appending, ", (i,j), ' to ', (ii,j+1), new_subtotal
				new_subtotals[(ii,j+1)] = new_subtotal
	subtotals = new_subtotals

print min(subtotals.values())