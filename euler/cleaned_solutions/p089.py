
# 55 minutes 
# In [69]: time %run p089.py
# 743
# CPU times: user 36 ms, sys: 4.98 ms, total: 41 ms
# Wall time: 47.3 ms


NUMERALS = {'I':1,
'V':5,
'X':10,
'L':50,
'C':100,
'D':500,
'M':1000}

SUBTRACTS = {
	'IV':4,
	'IX':9,
	'XL':40,
	'XC':90,
	'CD':400,
	'CM':900
}


from collections import Counter

def parse(numeral):
	"""
	Return integer value of numeral

	Assumes valid Roman numeral representation (see https://projecteuler.net/about=roman_numerals)
	assumes all subtracts only appear at most once
	"""
	# count all single letters
	single_counter = Counter(numeral)

	# check any subtracts, and subtract counts as necessary
	double_counts = []
	for subtract in SUBTRACTS.keys():
		if subtract in numeral:
			double_counts.append(subtract)
			for l in subtract:
				single_counter[l] -= 1

	single_counts = single_counter.items()
	# sum values
	total = 0
	for l,c in single_counts:
		total += NUMERALS[l]*c

	for ll in double_counts:
		total += SUBTRACTS[ll]

	return total


DIGIT_REPS = [
	None, #0!
	'o',
	'oo',
	'ooo',
	'of',
	'f',
	'fo',
	'foo',
	'fooo',
	'ot'
]


DIGIT_ENCODINGS = [{'o':'I','f':'V','t':'X'},
{'o':'X','f':'L','t':'C'},
{'o':'C','f':'D','t':'M'}]
#THOUSANDS IS A SPECIAL CASE!

def minimal_numeral(number):
	"""
	Return minimal roman numeral representation of 0 < number < 5000
	"""
	s_num = str(number)
	parts = []
	for dig,val in enumerate(reversed(s_num)):
		int_val = int(val)
		if dig == 3: #thousands special
			if int_val > 0:
				parts.insert(0,'M'*int_val)
		else:	
			rep = DIGIT_REPS[int_val]
			part = ''
			if rep == None:
				part = ''
			else:
				part = ''.join(DIGIT_ENCODINGS[dig][l] for l in rep)
			parts.insert(0,part)
	return ''.join(parts)




examples = """
MMMMDCLXXII
MMDCCCLXXXIII
MMMDLXVIIII
MMMMDXCV
DCCCLXXII
MMCCCVI
""".strip().split('\n')


for example in examples:
	print example, parse(example), minimal_numeral(parse(example))

def p89():
	with open('p089.txt','r') as f:
		numerals = f.read().strip().split('\n')

	total_dif = 0
	for numeral in numerals:
		orig = len(numeral)
		new = len(minimal_numeral(parse(numeral)))
		if new > orig:
			print "WHAT"
		else:
			total_dif += orig - new

	print total_dif

p89()





