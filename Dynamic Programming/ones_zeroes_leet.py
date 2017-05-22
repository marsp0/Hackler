'''https://leetcode.com/problems/ones-and-zeroes/#/description - MEDIUM'''
class Solution(object):
	def findMaxForm(self, strs, m, n):
		"""
		:type strs: List[str]
		:type m: int
		:type n: int
		:rtype: int
		"""
		memo = {}
		array = strs
		array = open('test.txt','r').read().strip()
		array = [v for v in array.split(',')]
		def count(string):
			one, zero = 0, 0
			for i in string:
				if i == '1':
					one += 1
				else:
					zero += 1
			return zero,one

		def recursive_memo(memo,index,m,n):
			if (index,m,n) in memo:
				return memo[(index,m,n)]
			else:
				if index == 0:
					zero,one = count(array[index])
					if m-zero >= 0 and n-one >= 0:
						memo[(index,m,n)] = 1
						return 1
					else:
						return 0
				else:
					zero,one = count(array[index])
					if m-zero >=0 and n-one >= 0:
						result = max(1+recursive_memo(memo,index-1,m-zero,n-one), recursive_memo(memo,index-1,m,n))
						memo[(index,m,n)] = result
						return result
					else:	
						result = recursive_memo(memo,index-1,m,n)
						memo[(index,m,n)] = result
						return result
		
		d = [count(array[i]) for i in xrange(len(array))]
		dp = [[0] * (n+1) for _ in xrange(m+1)]
		for i in xrange(len(d)):
			for j in xrange(m,-1,-1):
				for k in xrange(n,-1,-1):
					zero,one = d[i]
					if j-zero >= 0 and k-one >= 0:
						dp[j][k] = max(dp[j][k], dp[j-zero][k-one]+1)
		return dp[-1][-1]

p = Solution()
print p.findMaxForm(["0","1101","01","00111","1","10010","0","0","00","1","11","0011"],100,100)