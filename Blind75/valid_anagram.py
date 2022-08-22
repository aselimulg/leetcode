def isAnagram(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	if len(s) != len(t):
		return False
	letters = set(l for l in s)
	letter_dict = dict.fromkeys(letters, 0)
	for l in s:
		letter_dict[l] += 1
	
	letters2 = set(l for l in t)
	letter_dict2 = dict.fromkeys(letters2, 0)
	for l in t:
		letter_dict2[l] += 1

	for k in letter_dict:
		try:
			if letter_dict[k] != letter_dict2[k]:
				return False
		except:
			return False
	
	return True