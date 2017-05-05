'''https://leetcode.com/problems/maximum-subarray/ - Easy'''

class Solution(object):
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		max_ending_here = max_so_far = nums[0]
		for i in xrange(1,len(nums)):
			max_ending_here = max(nums[i], max_ending_here+nums[i])
			max_so_far = max(max_so_far,max_ending_here)
		return max_so_far