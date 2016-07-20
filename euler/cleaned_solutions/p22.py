
# 1 Brute
# Solve : 2 mins
# 1st Solution: 15 mins (total)

def word_score_ord(word):
	"""
	Computes alphabetical score of a word
	"""
	# lower case it
	lowered = word.lower()
	total = 0
	for l in lowered:
		total += ord(l) - 96
	return total

CHAR_SCORE = {'B': 2, 'D': 4, 'F': 6, 'H': 8, 'J': 10, 'L': 12, 'N': 14, 'P': 16, 'R': 18, 'T': 20, 'V': 22, 'X': 24, 'Z': 26, 'b': 2, 'd': 4, 'f': 6, 'h': 8, 'j': 10, 'l': 12, 'n': 14, 'p': 16, 'r': 18, 't': 20, 'v': 22, 'x': 24, 'z': 26, 'A': 1, 'C': 3, 'E': 5, 'G': 7, 'I': 9, 'K': 11, 'M': 13, 'O': 15, 'Q': 17, 'S': 19, 'U': 21, 'W': 23, 'Y': 25, 'a': 1, 'c': 3, 'e': 5, 'g': 7, 'i': 9, 'k': 11, 'm': 13, 'o': 15, 'q': 17, 's': 19, 'u': 21, 'w': 23, 'y': 25}
def word_score_raw(word):
	return sum(CHAR_SCORE[c] for c in word)

def word_score_raw_reduce(word):
	return reduce(lambda x,y: x + CHAR_SCORE[y], word, 0)




def brute(word_score_f=word_score_ord):

	with open("p022_names.txt",'r') as f:
		name_list = map(lambda x: x[1:-1],f.read().split(',')) #or strip?

	name_list.sort()

	total = 0
	for i, name in enumerate(name_list):
		total += (i + 1) * word_score_f(name)

# In [28]: %time brute(word_score)
# CPU times: user 14.4 ms, sys: 1.87 ms, total: 16.3 ms
# Wall time: 14.9 ms

# In [29]: %time brute(word_score_raw)
# CPU times: user 15 ms, sys: 2.29 ms, total: 17.3 ms
# Wall time: 15.7 ms

# In [30]: %time brute(word_score_raw_reduce)
# CPU times: user 21.1 ms, sys: 5.96 ms, total: 27.1 ms
# Wall time: 22.1 ms


#no way to "read to ,?"
	# NOT bottleneck
# what is bottleneck?
	# word_score...
		# In the cProfile, raw is the fastest 14ms cum, then ord at 15ms, then reduce at 19ms
	# Cannot find any real improvements...

if __name__ == '__main__':

	brute()