
# 55 mins!!!
# In [80]: time %run p54.py
# 376
# CPU times: user 86.4 ms, sys: 3.53 ms, total: 89.9 ms
# Wall time: 89.6 ms



from collections import Counter, defaultdict

VALUES = list('23456789TJQKA')
SUITS = list('HCSD')

hand = '5H 5C 6S 7S KD'.split(' ')

def sorted_card_vals(hand):
	return sorted([VALUES.index(c[0]) for c in hand], reverse=True)

def is_flush(hand):
	return len(set(c[1] for c in hand)) == 1

def get_combo_counts(hand):
	"""
	1s, 2s, 3s, 4s
	{}
	"""
	sorted_vals = sorted_card_vals(hand)
	counts = Counter(sorted_vals)
	combos = [[],[],[],[]]
	for val in sorted(counts.keys(), reverse=True):
		combos[counts[val]-1].append(val)
	return combos


def is_straight(hand):
	"""
	True if values of cards are consecutive vals of 5 cards
	"""
	sorted_vals = sorted(sorted_card_vals(hand))
	return sorted_vals == range(sorted_vals[0],sorted_vals[0]+5)

def get_encoding(hand):

	combos = get_combo_counts(hand)

	if is_straight(hand) and is_flush(hand):
		#10 RF
		sorted_vals = sorted_card_vals(hand)
		if sorted_vals[0] == 12:
			return (10,)
		# 9 SF
		else:
			return (9,sorted_vals[0])
	elif len(combos[3]) != 0:
		# get pc, hc
		return (8, combos[3][0], combos[0][0])
	elif len(combos[2]) == 1 and len(combos[1]) == 1:
		return (7, combos[2][0], combos[1][0])
	elif is_flush(hand):
		sorted_vals = sorted_card_vals(hand)
		sorted_vals.insert(0,6)
		return tuple(sorted_vals)
	elif is_straight(hand):
		sorted_vals = sorted_card_vals(hand)
		return (5,sorted_vals[0])
	elif len(combos[2]) == 1:
		return (4,combos[2][0],combos[0][0],combos[0][1])
	elif len(combos[1]) == 2:
		return (3,combos[1][0], combos[1][1],combos[0][0])
	elif len(combos[1]) == 1:
		return (2, combos[1][0], combos[0][0], combos[0][1], combos[0][2])
	else:
		sorted_vals = sorted_card_vals(hand)
		sorted_vals.insert(0,1)
		return tuple(sorted_vals)


p1_counts = 0
with open('p54_poker.txt','r') as f:
	rounds = map(str.strip,f.readlines())
	for a_round in rounds:
		cards = a_round.split(' ')
		p1hand, p2hand = cards[:5], cards[5:]
		if get_encoding(p1hand) > get_encoding(p2hand):
			p1_counts+=1

print p1_counts








