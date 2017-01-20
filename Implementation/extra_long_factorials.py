'''
	https://www.hackerrank.com/challenges/extra-long-factorials

	Note : this is DP
'''

import sys


n = int(raw_input().strip())

memo = {}

def factorial(n):
	try:
		return memo[n]
	except KeyError:
		if n == 1:
			memo[n] = 1
			return memo[n]
		elif n == 2:
			memo[n] = 2
			return memo[n]
		else:
			return n*factorial(n-1)

print factorial(n)