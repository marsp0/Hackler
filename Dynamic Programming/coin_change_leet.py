'''https://leetcode.com/problems/coin-change/#/description - medium'''

import sys
class Solution(object):
	def coinChange(self, array, target):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		memo = {}
		
		'''
		#top down with memoization TLE
		def recursive(memo,array,index,target):
			if (index,target) in memo:
				return memo[(index,target)]
			if target < 0:
				return sys.maxint
			elif target == 0:
				return 0
			elif index == 0:
				multiple = target / array[0]
				if array[0] * multiple != target:
					result = sys.maxint
				else:
					result = multiple
				#print result
				memo[(index,target)] = result
				return result
			else:
				if target - array[index] >= 0:
					result = min(1 + recursive(memo,array,index-1,target-array[index]),
						recursive(memo,array,index-1,target),
						1 + recursive(memo,array,index,target -array[index]))
				else:
					result = recursive(memo,array,index-1,target)
				memo[(index,target)] = result
				return result
		#use the below to call the recursive memoized function
		#Gives TLE after 125 test cases
		result = recursive(memo,array,len(array)-1,target)
		print len(memo)
		if result == sys.maxint:
			return -1
		else:
			return result

		# BOTTUM UP - TLE
		if target == 0:
			return 0
		for i in xrange(1,target+1):
			memo[(-1,i)] = sys.maxint
		for i in xrange(len(array)):
			for j in xrange(1,target+1):
				if array[i] == j:
					memo[(i,j)] = 1
				elif array[i] > j:
					memo[(i,j)] = memo[(i-1,j)]
				else:

					memo[(i,j)] = min(memo[(i-1,j)], memo[(i , j - array[i])]+1)
		result = memo[(len(array)-1,target)]
		print len(memo)
		if result == sys.maxint:
			return -1
		return result

		'''


		#solution with the help of the forums after I implemented the top down by myself. 
		dp = []
		max_element = float('inf')
		for i in xrange(target+1):
			if i == 0:
				dp.append(0)
			else:
				dp.append(max_element)
		for i in xrange(1,target+1):
			dp[i] = min(dp[i-coin] if i - coin >= 0 else max_element for coin in array) + 1
		if dp[target] == max_element:
			return -1
		else:
			return dp[target]

p = Solution()
print p.coinChange([2],3)