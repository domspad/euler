


#
# 1 - reverse path search
#
# 30 mins for idea
# 1 hr for code

# In [2]: %time p81(fname, skiprows)
# CPU times: user 38.8 ms, sys: 1.9 ms, total: 40.7 ms
# Wall time: 49 ms
# Out[2]: 427337.0


def diag_indicies(k, n):
	"""
		0 <= k < 2n-1
	return all cell indicies in the kth diag of a n x n matrix
		diag_indices(5,5) = [(1,4), (2,3), (3,2), (4,1)]

		all partitions of k into two integers between 0,n-1
	"""

	partitions = [(i, k-i) for i in xrange(k+1)]
	return filter(lambda idx: idx[0] < n and idx[1] < n, partitions)



def child_indicies(idx, n):
	"""
		idx valid index in n x n matrix
	return cell indices of valid right/down moves for given cell idx

		(1,4),5 --> 
	"""
	children = [(idx[0]+1,idx[1]), (idx[0],idx[1]+1)]
	return filter(lambda ix: ix[0]<n and ix[1]<n, children)


import numpy as np

fname = 'p081_matrix.txt'
skiprows = 0

def p81(fname=fname,skiprows=skiprows):

	# read in matrix
	with open(fname, 'rb') as f:
		mat = np.loadtxt(f,delimiter=",",skiprows=skiprows)

	# initialize new 0s matrix
	n = mat.shape[0]
	ndiag = sum(mat.shape)
	subsum = np.zeros(mat.shape)
		# start with last cell initialized
	subsum[-1,-1] = mat[-1,-1]

	# iterate from last 2nth row to top
	for i in xrange(ndiag-3,-1,-1):
		# for all cells in ith diag
		for idx in diag_indicies(i, n):
			# set subsum cell equal to mat cell + smallest child cell in subsum
			subsum[idx] = mat[idx] + min(subsum[child_idx] for child_idx in child_indicies(idx, n))

	return subsum[0,0]



##########################################v TESTS
# return first element
set(diag_indicies(7,5)) == set([(3,4), (4,3)])
set(diag_indicies(2,5)) == set([(0,2), (1,1), (2,0)])
set(diag_indicies(0,5)) == set([(0,0)])
set(diag_indicies(8,5)) == set([(4,4)])

	
child_indicies((1,4),5) == [(2,4)]
