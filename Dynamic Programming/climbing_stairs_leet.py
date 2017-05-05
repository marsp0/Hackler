'''https://leetcode.com/problems/climbing-stairs/#/description - Easy'''

class Solution(object):
	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		memo = {1:1,2:2}
		return self.calculate(n,memo)

	def calculate(self,n,memo):
		if n in memo:
			return memo[n]
		else:
			result = self.calculate(n-1,memo) + self.calculate(n-2,memo)
			memo[n] = result
			return result