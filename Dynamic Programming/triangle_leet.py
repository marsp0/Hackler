'''https://leetcode.com/problems/triangle/#/description - MEDIUM'''

class Solution(object):
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		memo = {}
		for col in xrange(len(triangle[-1])):
			memo[(len(triangle)-1,col)] = triangle[-1][col]
		for i in xrange(len(triangle)-2,-1,-1):
			for j in xrange(len(triangle[i])):
				memo[(i,j)] = min(memo[(i+1,j)], memo[(i+1,j+1)]) + triangle[i][j]
		return memo[(0,0)]

p = Solution()
print p.minimumTotal([
	 [2],
	[3,4],
   [6,5,7],
  [4,1,8,3]
])