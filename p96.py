

# 55 mins so far (for no guess needed solutions)
# 85 mins TOTAL 
# Functional-ish brute force
# In [11]: %time %run p96.py
# 24702
# CPU times: user 20.4 s, sys: 306 ms, total: 20.7 s
# Wall time: 21.5 s

from pprint import pprint

def grids(f):
	"""
	generator of grids
	"""
	while True:
		line = f.readline()
		if not line:
			raise StopIteration
		else:
			yield [map(int,f.readline().strip()) for newrow in xrange(9)]

def sq_idxs(i,j):
	i_start = (i/3) * 3
	j_start = (j/3) * 3
	for ii in xrange(i_start, i_start+3):
		for jj in xrange(j_start, j_start+3):
			yield (ii,jj)

def update_cands(i,j,v,candidates):
	"""
	side effects on candidates given new assignemnt of grid[i][j] = v
	"""
	for jx in xrange(9):
		if jx != j:
			candidates[(i,jx)] -= {v}
	# col 
	for ix in xrange(9):
		if ix != i:
			candidates[(ix,j)] -= {v}
	# sq
	for ix,jx in sq_idxs(i,j):
		if i != ix or j != jx:
			candidates[(ix,jx)] -= {v}

def get_move(game_state):
	"""
	get i,j with least available options
	"""
	candidates = game_state.candidates
	unset = game_state.unset

	least = 10
	for i,j in unset:
		if len(candidates[(i,j)]) <= least:
			mi,mj = i,j
			least = len(candidates[(i,j)])
	if least == 10:
		raise ValueError('something has gone horribly wrong')
	return mi,mj

def is_valid(game_state):
	"""
	False if there is an i,j with 0 available candidates
	"""
	# TODO: are there any other "invalid" game states?
	return not any(len(game_state.candidates[(i,j)]) == 0 for i,j in game_state.candidates)
# game_state == 

class GameState(object):
	"""
	Just a struct to hold game state
	"""
	
	def __init__(self, grid, candidates, unset):
		self.grid = grid
		self.candidates = candidates
		self.unset = unset


from copy import deepcopy

def make_move(game_state):
	"""
	Assumes game_state is valid and is not goal
	Returns a list of updated game states or empty list if theres a contradiction
	"""
	candidates = game_state.candidates
	unset = game_state.unset
	grid = game_state.grid

	# get unset i,j with least candidates
	i,j = get_move(game_state)
	cands = game_state.candidates[(i,j)]

	# create new gamestates for each candidate
	new_game_states = []

	for v in cands:
		gs = deepcopy(game_state)

		# make move 
		gs.unset.remove((i,j))
		gs.grid[i][j] = v
		update_cands(i,j,v,gs.candidates)

		new_game_states.append(gs)

	return new_game_states


def is_goal(game_state):
	return len(game_state.unset) == 0

with open('p96_hardest.txt','r') as f:
	c = 0
	hashsum = 0
	for grid in grids(f):
		# initialize grid, candidates, unset with starting positions
		candidates = dict(((i,j),set(xrange(1,10))) for i in xrange(9) for j in xrange(9))
		unset = set([(i,j) for i in xrange(9) for j in xrange(9)])
		for i in xrange(9):
			for j in xrange(9):
				v = grid[i][j]
				if v != 0:
					candidates[(i,j)] = set([v])
					update_cands(i,j,v,candidates)
					unset -= {(i,j)}
		
		# DETERMINISTIC solution
		# while any candidates have len == 1 and not set, 
		game_state_stack = [GameState(grid, candidates, unset)]

		while len(game_state_stack) != 0:
			game_state = game_state_stack.pop()
			if is_goal(game_state):
				print "SOLVED"
				hashsum += int(''.join(map(str,game_state.grid[0][:3])))
				pprint(game_state.grid)
				print hashsum
				c += 1
				break

			else:
				if not is_valid(game_state):
					continue
				else: #add fringe gamestates to stack
					game_state_stack.extend(make_move(game_state))


		# while len(unset) != 0:
		# 	try:
		# 		(i,j) = get_move(candidates, unset)
		# 	except ValueError:
		# 		print "NOT SOLVABLE NOW"
		# 		print len(unset), grid
		# 		break
		# 	# make move
		# 	v = candidates[(i,j)].pop()
		# 	candidates[(i,j)].add(v)
		# 	unset.remove((i,j))
		# 	grid[i][j] = v
		# 	update_cands(i,j,v,candidates)
		# if len(unset) == 0:
		# 	print "SOLVED"
		# 	pprint(grid)
		# 	c+=1
	print c
