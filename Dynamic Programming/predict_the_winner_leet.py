class Solution(object):
	def PredictTheWinner(self, array):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		self.array = array
		memo = {}
		result = self.recursive(memo,0,len(array)-1)
		sum_elements = sum(self.array)
		if sum_elements - result > result:
			return False
		else:
			return True
	
	def recursive(self,memo,i,j):
		if (i,j) in memo:
			return memo[(i,j)]
		else:
			if self.array[i:j+1] == []:
				result = 0
				memo[(i,j)] = result
				return result
			if i == j:
				memo[(i,j)] = self.array[i]
				return memo[(i,j)]
			elif j - i == 1:
				result = max(self.array[i], self.array[j])
				memo[(i,j)] = result
				return result
			else:
				result = max( 	min(self.recursive(memo, i+1, j-1), 
									self.recursive(memo, i+2, j)
									) + self.array[i],

								min(self.recursive(memo, i, j-2),
									self.recursive(memo,i+1,j-1)
									) + self.array[j]
					)
				memo[(i,j)] = result
				return result

p = Solution()
print p.PredictTheWinner([1, 5, 2])