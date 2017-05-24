'''https://leetcode.com/problems/partition-equal-subset-sum/#/description - Medium'''

class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		array = sorted(nums,reverse=True)
		sum_elements = sum(nums)

		if sum_elements % 2 == 1:
			return False
		else:
			memo = {}
			def recursive(memo,array,target,start):
				if target in memo:
					return memo[target]
				if target == 0:
					memo[target] = True
					return True
				else:
					memo[target] = False
					for i in xrange(start,len(array)):
						if recursive(memo,array,target-array[i],i+1):
							memo[target] = True
							break
				return memo[target]
			return recursive(memo,array,sum_elements/2,0)

class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		nums = sorted(nums,reverse=True)
		sum_elements = sum(nums)
		print len(nums)
		if sum_elements % 2 == 1:
			return False
		else:
			memo = {}
			def recursive(memo,array,index,S):
				if (index,S) in memo:
					return memo[(index,S)]
				if S <= 0:
					return 0
				if index == 0:
					if S - array[0] >= 0:
						memo[(index,S)] = array[0]
					else:
						memo[(index,S)] = 0
					return memo[(index,S)]
				else:
					if S - array[index] >= 0:
						result = max(array[index] + recursive(memo,array,index-1,S-array[index]), recursive(memo,array,index-1,S))
					else:
						result = recursive(memo,array,index-1,S)
					memo[(index,S)] = result
					return result
		result = recursive(memo,nums,len(nums)-1,sum_elements/2)
		if result != sum_elements/2:
			return False
		return True

p = Solution2()
print p.canPartition([80,38,97,19,81,96,70,35,12,44,33,51,78,86,31,74,94,54,11,91,7,90,83,12,91,67,40,80,39,87,17,49,66,56,15,99,95,91,22,49,14,23,18,74,22,62,14,94,75,97,45,32,9,21,14,70,93,14,91,6,99,12,29,32,26,33,44,24,82,84,95,10,91,38,23,27,64,88,83,85,7,23,62,49,60,67,31,55,87,42,61,4,7,10,12,8,94,9,30,59])

p = Solution()
print p.canPartition([80,38,97,19,81,96,70,35,12,44,33,51,78,86,31,74,94,54,11,91,7,90,83,12,91,67,40,80,39,87,17,49,66,56,15,99,95,91,22,49,14,23,18,74,22,62,14,94,75,97,45,32,9,21,14,70,93,14,91,6,99,12,29,32,26,33,44,24,82,84,95,10,91,38,23,27,64,88,83,85,7,23,62,49,60,67,31,55,87,42,61,4,7,10,12,8,94,9,30,59])