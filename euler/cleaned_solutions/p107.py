

# building minimal tree
# 68 mins
# In [1]: %time %run p107.py
# 259679
# CPU times: user 4.82 ms, sys: 871 µs, total: 5.69 ms
# Wall time: 5.43 ms

def p107():	
	# compute N and generate sorted edge_list [(edge,weight),...]
	edge_list = []
	with open('p107.txt', 'r') as f:
		lines = f.readlines()
		N = len(lines)
		for x, line in enumerate(lines):
			for y, weight in enumerate(line.strip().split(',')):
				if weight == '-':
					pass
				else:
					edge_list.append( (int(weight), (x,y))  )
	edge_list.sort(key=lambda pair: pair[0])

	# generate connected_components dict(node: its_connected_component)
	connected_components = dict((i, set((i,))) for i in xrange(N))


	total_weight = sum(zip(*edge_list)[0]) / 2 # double counting because in form of array!
	tree_edge_num = N - 1 # via theorem
	num_edges = 0
	tree_weight = 0
	for weight, edge in edge_list:
		x,y = edge
		if connected_components[x] != connected_components[y]:
			# add the edge to the final set by combining x,y connected components
			new_component = connected_components[x] | connected_components[y]
			for node in new_component:
				connected_components[node] = new_component
			num_edges += 1
			tree_weight += weight
			if num_edges == tree_edge_num:
				break

	print total_weight - tree_weight

p107()

