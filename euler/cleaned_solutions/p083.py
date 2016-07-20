
#90 mins in still no complete solution
	# there is recursive/dynamic programming way but can't find way to state it without 
		# a) having subproblems referring to each other
			# e.g. min path to each node is minimum of min path to each neighbor node 
		# OR
		# b) having exponentially many subproblems
			# e.g. constructing minimial paths excluding parent nodes, but that is equal to number of unique paths anyway


# 3 hours - dynamic programming solution
	# recognized applicability of Bellman-Ford shortest path from single source
# In [15]: time %run p083.py
# 425185.0
# CPU times: user 18min 8s, sys: 12.4 s, total: 18min 20s
# Wall time: 18min 44s

case_ans = {'p083_small.txt':2297,
			'p083_small2.txt':17,
			'p083_small3.txt':17}
			# 'p082_matrix.txt':


SPECIAL = 10**10
import numpy as np

def is_invalid((i,j)):
	return i < 0 or i >= N or j < 0 or j >= N

def get_neighbors(i,j):
	"""	
	assumes N in global namespace
	gets all neighbor cells to (i,j) in NxN matrix
	"""
	neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

	return filter(lambda x: not is_invalid(x),neighbors	 )



with open('p083_matrix.txt', 'r') as f:
	mat = np.loadtxt(f,delimiter=",").tolist()
	M = len(mat)
	N = len(mat[0])
	total = sum(map(sum,mat))
# (N X N) X N^2 matrix (ASSUMES N == M)
# min_path_mat = [[[np.nan]*N]*N]*(N**2)      #ERROR SAME LIST!!!!
min_path_mat = [[[np.nan for i in xrange(N)] for j in xrange(N)] for k in xrange(N**2)]
		   # k  i  j
min_path_mat[0][0][0] = mat[0][0]

assert len(get_neighbors(0,0)) == 2

def p83():
	for k in xrange(1,N**2):
		print 1.*k/(N**2)
		for i in xrange(N):
			for j in xrange(N):
				neighbors = get_neighbors(i,j)
				# get minimum
				current = min_path_mat[k-1][i][j]
				# if np.isnan(current):
				# 	current = 10
				neighbors_extended = [min_path_mat[k-1][u][v] for u,v in neighbors]
				neighbors_extended = map(lambda x: x + mat[i][j] if not np.isnan(x) else np.nan, neighbors_extended)
				candidates = neighbors_extended + [current]
				new_current = reduce(lambda x,y: min(x,y) if not np.isnan(y) else x, candidates,SPECIAL)
				if new_current == SPECIAL: #then all were np.nan
					new_current = np.nan
				min_path_mat[k][i][j] = new_current
		# update min_path to cells of length <= k

	return min_path_mat[-1][-1][-1]

print p83()
