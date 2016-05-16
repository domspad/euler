
# 2 hours to complete
# simulation solution to get probabilities (first corraborate results with 6-sided, then used that number of trials to get 4-sided)
# NOTE: BECAUSE statistically, not right all the time!!! e.g.
# In [1]: time %run p84.py
# [(10, 598015), (24, 326810), (15, 325691)]
# CPU times: user 1min 3s, sys: 522 ms, total: 1min 4s
# Wall time: 1min 5s

#Params
sides = 4


from collections import Counter
die_tuples = map(lambda x: (x[0],x[1]/float(sides**2)),Counter(map(sum,[(i,j) for i in xrange(1,sides+1) for j in xrange(1,sides+1)])).items())


G2J = 30
CC1 = 2
CC2 = 17
CC3 = 33
CCs = [CC1,CC2,CC3]
CH1 = 7
CH2 = 22
CH3 = 36
CHs = [CH1,CH2,CH3]
JAIL = 10
GO = 0
Rs = [5, 15, 25, 35]
Us = [12, 28]
# Compute Move Matrix 

import numpy as np

move_mat = np.zeros((40,40))
	# compute die roll matrix
for i in xrange(40):
	for roll, prob in die_tuples:
		new_i = (i+roll)%40
		if new_i == G2J:
			move_mat[i,JAIL] = prob
		else:
			move_mat[i,new_i] = prob

	# adjust for special cells

		# G2J
move_mat[G2J] = 0
move_mat[:,G2J] = 0

		# CC's
for i in xrange(40):

	for CC in CCs:
		prob = move_mat[i,CC]
		if prob != 0:
			move_mat[i,CC] *= (14./16)
			move_mat[i,GO] += prob * (1./16)
			move_mat[i,JAIL] += prob * (1./16)



		# CH's
	for CH in CHs:
		prob = move_mat[i,CH]
		if prob != 0:
			move_mat[i,CH] *= (6./16)
			to_adjust = [GO, JAIL, 11, 24, 39, 5] #C1, E3, H2, R1
			#next R twice
			if i < 5:
				to_adjust.append(5)
				to_adjust.append(5)
			elif i < 15:
				to_adjust.append(15)
				to_adjust.append(15)
			elif i < 25:
				to_adjust.append(25)
				to_adjust.append(25)
			elif i < 35:
				to_adjust.append(35)
				to_adjust.append(35)
			else:
				to_adjust.append(5)
				to_adjust.append(5)

			#next U
			if i < 12:
				to_adjust.append(12)
			elif i < 28:
				to_adjust.append(28)
			else:
				to_adjust.append(12)

			#3 backwards
			backwards = (CH - 3) % 40
			#FIXME: NEED TO ADJUST IF backwards == 33 (then another CC square!)
			to_adjust.append(backwards)

			for j in to_adjust:
				move_mat[i,j] += prob * (1./16)

		# (doesnt account for 3 double rolls --> Jail)

# Given starting vector (which?), compute ~1000 moves, see end result

	# try all cells equal first
all_equal = np.array([1/40.]*40)
updated = all_equal
for turn in xrange(100):
	updated = move_mat.dot(updated)
	# if (updated > 1).any() or (updated < 0).any():
	# 	# print turn, 'what'

	# try with first turn vector
first_turn = np.zeros((40,))
first_turn[0] = 1.
updated = first_turn
for turn in xrange(1000):
	updated = move_mat.dot(updated)


# move_mat[0] is first row
#axis = 1 is summing acros row
move_mat.sum(1)

# trying simulations....17:26
cum_mat = move_mat.cumsum(axis=1)
id_mat = np.array(xrange(40))
c = Counter()
i = 0


def move(i):
	"""
	Move from square i to another square
	"""
	r = np.random.rand()
	return id_mat[cum_mat[i] > r][0]

for turn in xrange(10000000):
	c[i] += 1
	i = move(i)

print c.most_common(3)

sorted(map(lambda x: (x[0],x[1]/10000000.),map(list,c.items())),key=lambda x:x[1],reverse=True)[:3]