'''https://leetcode.com/problems/longest-palindromic-subsequence/#/description - MEDIUM'''

from collections import defaultdict

class Solution(object):
	def longestPalindromeSubseq(self, string):
		"""
		:type s: str
		:rtype: int
		"""
		if string == string[::-1]:
			return len(string)
		elif string == '':
			return 0
		memo = defaultdict(dict)
		def recursive(memo,string,start,end):
			if start in memo and end in memo[start]:
				return memo[start][end]
			else:
				if start > end:
					result = 0
				elif (end+1 - start) == 0:
					result = 0
				elif start == end:
					result = 1
				else:
					if string[start] == string[end]:
						result = 2 + recursive(memo,string,start+1,end-1)
					else:
						result = max(recursive(memo,string,start,end-1),recursive(memo,string,start+1,end))
				memo[start][end] = result
				return result
		return recursive(memo,string,0,len(string)-1)

p = Solution()
print p.longestPalindromeSubseq('cbbd')
