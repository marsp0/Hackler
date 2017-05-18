''' https://leetcode.com/problems/house-robber/#/description - easy '''

class Solution(object):
	def rob(self, array):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		rob = [0] * len(array)
		rest = [0] * len(array)
		if len(array) > 0:
			for i in xrange(len(array)):
				rob[i] = max(rest[i-1] + array[i], rob[i-1])
				rest[i] = max(rest[i-1], rob[i-1])
			return max(rob[-1],rest[-1])
		return 0