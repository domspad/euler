

# Bt clunky brute force with some precomputation
# 70 mins
# In [136]: %time %run p98.py
# (17689, 18769)
# CPU times: user 11.9 s, sys: 105 ms, total: 12 s
# Wall time: 12.1 s


def alphabet_gen():
	for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		yield l

def pattern(string):
	"""
	RACER --> "ABCDA"
	'10124' --> "ABACD"
	"""
	mapping = {}
	pattern = []
	alphabet = alphabet_gen()
	for c in string:
		if c not in mapping:
			mapping[c] = next(alphabet)
		pattern.append(mapping[c])
	return ''.join(pattern)

def pattern_mapping(string):
	pat = pattern(string)
	return dict((k,w) for k,w in zip(string,pat))

def map_maker(mapping):
	def mapper(word):
		return ''.join( (str(mapping[c]) for c in word))
	return mapper

# read in words
with open('p98_words.txt','r') as f:
	words = [quoted.strip('"') for quoted in f.read().split(',')]
	
# set of anagrams by sorted letters
sorted_words = [tuple(sorted(w)) for w in words]


from collections import Counter, defaultdict

anags = defaultdict(list)
for sw,w in zip(sorted_words,words):
	anags[sw].append(w)

atleast2 = dict( ( (k,w) for k,w in anags.iteritems() if len(w) > 1))

max_len = max([len(w) for w in atleast2])


from itertools import combinations
ANAGRAM_PAIRS = []
for sw, w in atleast2.iteritems():
	if len(w) == 2:
		ANAGRAM_PAIRS.append(w)
	else:
		ANAGRAM_PAIRS.extend(combinations(w,2))


# up too all 9-digit square numbers (that is longest word)
SQUARES = set([n**2 for n in xrange(100000)])
sq_anags = defaultdict(list)
sorted_squares = [tuple(sorted(str(i))) for i in SQUARES]
for sw, w in zip(sorted_squares,SQUARES):
	sq_anags[sw].append(w)

atleast2_sq = dict( ( (k,w) for k,w in sq_anags.iteritems() if len(w) > 1))

SQ_ANAGRAM_PAIRS = []
for sw, w in atleast2_sq.iteritems():
	if len(w) == 2:
		SQ_ANAGRAM_PAIRS.append(w)
	else:
		SQ_ANAGRAM_PAIRS.extend(combinations(w,2))




ANAGRAM_PATTERN_PAIRS = set()
for ws in ANAGRAM_PAIRS:
	mapping = pattern_mapping(ws[0])
	mapper = map_maker(mapping)
	ANAGRAM_PATTERN_PAIRS.add(tuple(map(mapper,ws)))


SQ_ANAGRAM_PATTERN_PAIRS = set()
for nums in SQ_ANAGRAM_PAIRS:
	str_nums = map(str,nums)
	mapper = map_maker(pattern_mapping(str_nums[0]))
	SQ_ANAGRAM_PATTERN_PAIRS.add(tuple(map(mapper,str_nums)))


longest_pat_pair = max(ANAGRAM_PATTERN_PAIRS & SQ_ANAGRAM_PATTERN_PAIRS)

for nums in SQ_ANAGRAM_PAIRS:
	str_nums = map(str,nums)
	mapper = map_maker(pattern_mapping(str_nums[0]))
	pat_pair = tuple(map(mapper,str_nums))
	if pat_pair == longest_pat_pair:
		print nums
