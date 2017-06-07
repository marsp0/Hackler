'''Thanks to Twitch chat'''
'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description - Easy'''

class Solution(object):
	def maxProfit(self, array):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		index = 0
		result = 0
		while index < len(array)-1:
			if array[index] < array[index + 1]:
				result += (array[index+1] - array[index])
			index += 1
		return result

p = Solution()
print p.maxProfit([1,2,4])