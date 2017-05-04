'''https://leetcode.com/problems/range-sum-query-immutable/ - Easy'''

class NumArray(object):

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums
		self.table = [0]*len(self.nums)
		if len(self.nums) > 0:
			self.table[0] = self.nums[0]
			for i in xrange(1,len(self.nums)):
				self.table[i] = self.table[i-1] + self.nums[i]

	def sumRange(self, i, j):
		"""
		:type i: int
		:type j: int
		:rtype: int
		"""
		if i == 0:
			return self.table[j]
		else:
			return self.table[j] - self.table[i-1] 
