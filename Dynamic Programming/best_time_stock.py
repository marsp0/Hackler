'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description - Easy'''

class Solution(object):
	def maxProfit(self, array):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		result = 0
		if array:
			min_element = array[0]
			for i in xrange(len(array)):
				if array[i] < min_element:
					min_element = array[i]
				else:
					if array[i] - min_element > result:
						result = array[i] - min_element
		return result