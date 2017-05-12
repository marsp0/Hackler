'''https://leetcode.com/problems/minimum-path-sum/#/description - Medium'''

class Solution(object):

	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		memo = {}
		for i in xrange(len(grid)):
			for j in xrange(len(grid[0])):
				if i == 0 and j == 0:
					memo[(i,j)] = grid[i][j]
				elif i == 0 and j != 0:
					memo[(i,j)] = memo[(i,j-1)] + grid[i][j]
				elif i != 0 and j == 0:
					memo[(i,j)] = memo[(i-1,j)] + grid[i][j]
				else:
					memo[(i,j)] = min(memo[(i-1,j)], memo[(i,j-1)]) + grid[i][j]
		#print memo
		return memo[(len(grid)-1,len(grid[0])-1)]

p = Solution()
print p.minPathSum([[0,1],[1,0]])