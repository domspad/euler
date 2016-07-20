
# 10 minutes
# In [45]: time %run p42.py
# 162
# CPU times: user 10.9 ms, sys: 4.99 ms, total: 15.9 ms
# Wall time: 21.1 ms

with open('p42_words.txt','r') as f:
	words = f.read().strip('"').split('","')


letter_num_map = dict( (c,i+1) for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

tri_nums = set([n * (n+1) / 2 for n in xrange(1,30)])


def word_to_num(word):
	"""
	'SKY' --> 55
	"""
	return sum(letter_num_map[w] for w in word)

def is_tri_word(word):
	"""
	if SKY == 55 is a triangular number
	"""
	return word_to_num(word) in tri_nums

print len(filter(is_tri_word,words))
