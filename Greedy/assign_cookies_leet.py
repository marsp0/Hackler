'''https://leetcode.com/problems/assign-cookies/#/description - EASY'''

class Solution(object):
	def findContentChildren(self, greed, cookies):
		"""
		:type g: List[int]
		:type s: List[int]
		:rtype: int
		"""
		greed = sorted(greed)
		cookies = sorted(cookies)
		index_cookie = 0
		index_child = 0
		counter = 0
		while True:
			try:
				if cookies[index_cookie] >= greed[index_child]:
					index_child += 1
					index_cookie += 1
					counter += 1
				else:
					index_cookie += 1
			except IndexError:
				break
		return counter

p = Solution()
print p.findContentChildren([1,2], [1,2,3])