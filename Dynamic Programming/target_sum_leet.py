'''https://leetcode.com/problems/target-sum/#/description - Medium'''

class Solution(object):
	def findTargetSumWays(self, array, S):
		"""
		:type nums: List[int]
		:type S: int
		:rtype: int
		"""
		memo = {}
		return self.recursive(memo,array,S)

	def recursive(self,memo,array,S):
		if (len(array),S) in memo:
			return memo[(len(array),S)]
		else:
			if len(array) == 0:
				result = 0
				if S == 0:
					result = 1
			else:
				result = self.recursive(memo,array[:-1],S-array[-1]) + self.recursive(memo,array[:-1],S+array[-1])
			memo[(len(array),S)] = result
			return result

p = Solution()
print p.findTargetSumWays([1, 1, 1, 1, 1],3)
