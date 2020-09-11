def lengthOfLongestSubstring(self, s):
	hash_table = {}
	maxLength = 0
	start = 0

	for i in range(len(s)):

		if (s[i] in hash_table): 
			start = max(start, hash_table[s[i]]+1)

		maxLength = max(maxLength,i-start+1)
		hash_table[s[i]]=i

	return maxLength