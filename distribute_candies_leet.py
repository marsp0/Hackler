'''https://leetcode.com/problems/distribute-candies/#/description - easy'''

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        hash_table = {}
        for item in candies:
            if item not in hash_table:
                hash_table[item] = 1
            else:
                hash_table[item] += 1
        return min(len(hash_table),len(candies)/2)