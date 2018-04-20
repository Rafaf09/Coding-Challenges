def anagram_check(word1, word2):
	"""Returns true if word1 and word2 are anagrams
	(the letters of one input can rearrange into the other input),
	false otherwise.


	>>> anagram_check("parliament", "partial men")
	True

	>>> anagram_check("hello", "goodbye")
	False

	>>> anagram_check("snake", "ekans")
	True
	"""

	word1 = word1.replace(" ", "")
	word2 = word2.replace(" ", "")
	dict1 = {}
	dict2 = {}

	for letter in word1:
		if letter.lower() not in dict1:
			dict1[letter.lower()] = 1
		else:
			dict1[letter.lower()] += 1

	for letter in word2:
		if letter.lower() not in dict1:
			return False
		elif letter.lower() not in dict2:
			dict2[letter.lower()] = 1
		else:
			dict2[letter.lower()] += 1

	return dict1 == dict2

