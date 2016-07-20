


# Precomputed edges of graph network and then depth first brute over paths
# In [59]: %time %run p61.py
# 28684
# CPU times: user 73.7 ms, sys: 8.12 ms, total: 81.8 ms
# Wall time: 76.6 ms

#2:24
SETS = {'t':set(str(n*(n+1)/2) for n in xrange(1000) if len(str(n*(n+1)/2)) == 4 ),
's':set(str(n**2) for n in xrange(1000) if len(str(n**2)) == 4 ),
'p':set(str(n*(3*n-1)/2) for n in xrange(1000) if len(str(n*(3*n-1)/2)) == 4 ),
'h':set(str(n*(2*n-1)) for n in xrange(1000) if len(str(n*(2*n-1))) == 4 ),
'u':set(str(n*(5*n-3)/2) for n in xrange(1000) if len(str(n*(5*n-3)/2)) == 4 ),
'o':set(str(n*(3*n - 2)) for n in xrange(1000) if len(str(n*(3*n - 2))) == 4 )}

# edges
EDGES = {}
for group in SETS:
	for num in SETS[group]:
		EDGES[(num,group)] = []
		for group2 in SETS:
			if group == group2:
				continue
			else:
				for num2 in SETS[group2]:
					if num2.startswith(num[-2:]):
						EDGES[(num,group)].append((num2,group2))


def get_edges(solution_stack):
	used_keys = ''.join(x[1] for x in solution_stack)
	last_one = solution_stack[-1]
	return [cand for cand in EDGES[last_one] if cand[1] not in used_keys]

def p61():
	solution_stack = []
	for num in SETS['o']:
		# print num
		solution_stack.append((num,'o'))
		for cand in get_edges(solution_stack):
			solution_stack.append(cand)
			for cand2 in get_edges(solution_stack):
				solution_stack.append(cand2)
				for cand3 in get_edges(solution_stack):
					solution_stack.append(cand3)
					for cand4 in get_edges(solution_stack):
						# print solution_stack, cand4
						solution_stack.append(cand4)
						for cand5 in get_edges(solution_stack):
							# print solution_stack, cand5
							if solution_stack[0][0].startswith(cand5[0][-2:]):
								solution_stack.append(cand5)
								return sum(int(x[0]) for x in solution_stack)
						solution_stack.pop()
					solution_stack.pop()
				solution_stack.pop()
			solution_stack.pop()
		solution_stack.pop()
	# print solution_stack

print p61()

# ALL_SETS = [(n,k) for k in SETS for n in SETS[k]]

# def remaining_cands(sol):

# 	used_keys = set(x[1] for x in sol)
# 	return filter(lambda x: x[0].startswith(sol[-1][0][-2:]) and x[1] not in used_keys, ALL_SETS)

# for num in SETS['o']:
# 	sol = [(num,'o')]
# 	cands = remaining_cands(sol)
# 	if len(cands) == 0:
# 		sol.pop()
# 		continue
# 	for i,k in cands:
# 		sol.append((i,k))
# 		cands2 = remaining_cands(sol)
# 		if len(cands2) == 0:
# 			sol.pop()
# 			continue
# 		for ii,kk in cands2:
# 			sol.append((ii,kk))
# 			cands3 = remaining_cands(sol)
# 			if len(cands3) == 0:
# 				sol.pop()
# 				continue
# 			for iii,kkk in cands3:
# 				sol.append((iii,kkk))
# 				cands4 = remaining_cands(sol)
# 				if len(cands4) == 0:
# 					sol.pop()
# 					continue
# 				for iiii,kkkk in cands4:
# 					sol.append((iiii,kkkk))
# 					cands5 = remaining_cands(sol)
# 					if len(cands5) == 0:
# 						sol.pop()
# 						continue
# 					for iiiii,kkkkk in cands5:
# 						sol.append((iiiii,kkkkk))
# 						cands2 = remaining_cands(sol)
# 						if len(cands2) == 0:
# 							sol.pop()
# 							continue
# 						break
						

# # 	for i,k in remaining_cands(sol):
# # 		sol.append()
# # 	filter(lambda x: x[1].startswith())

# # 	while len(sol) != 6:
# # 		try:
# # 			extend(sol)
# # 		except ValueError:
# # 			break
# # 	if len(sol) == 6:
# # 		print sol
# # 		break


# # def extend(solution):
# # 	"""

# # 	"""
# # 	start = num[-2:]
# # 	remaining_sets = 