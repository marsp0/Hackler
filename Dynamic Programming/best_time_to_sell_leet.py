'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/#/description - MEDIUM'''

class Solution(object):
	def maxProfit(self, array):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if len(array) == 0:		
			return 0
		sell = [0] * len(array)
		buy = [0] * len(array)
		buy[0] = -array[0]
		sell[0] = 0
		cooldown = [0] * len(array)
		cooldown[0] = 0
		for i in xrange(1,len(array)):
			buy[i] = max(buy[i-1],cooldown[i-1]-array[i])
			sell[i] = max(buy[i-1]+array[i],sell[i-1])
			cooldown[i] = max(sell[i-1],buy[i-1],cooldown[i-1])
		return max(buy[-1],sell[-1],cooldown[-1])


p = Solution()
print p.maxProfit([1, 2, 3, 0, 2])