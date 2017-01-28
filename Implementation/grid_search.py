#!/bin/python

'''https://www.hackerrank.com/challenges/the-grid-search'''

import sys

class RaiseIt(BaseException):
	pass


t = int(raw_input().strip())
tests = {}
for a0 in xrange(t):
	R,C = raw_input().strip().split(' ')
	R,C = [int(R),int(C)]
	G = []
	G_i = 0
	for G_i in xrange(R):
		G_t = str(raw_input().strip())
		G.append(G_t)
	r,c = raw_input().strip().split(' ')
	r,c = [int(r),int(c)]
	P = []
	P_i = 0
	for P_i in xrange(r):
		P_t = str(raw_input().strip())
		P.append(P_t)
	tests[a0] = (G,P)

results = []

for test in tests:
	grid = tests[test][0]
	pattern = tests[test][1]
	temp_string = ''
	try:
		for row in xrange(len(grid)):
			for column in xrange(len(grid[row])):
				temp = 1
				if grid[row][column] == pattern[0][0]:
					try:
						if grid[row][column:column+len(pattern[0])] == pattern[0]:
							for j in xrange(1,len(pattern)):
								if grid[row+j][column:column+len(pattern[0])] == pattern[j]:
									temp += 1
								else:
									break
							if temp >= len(pattern):
								temp_string = 'YES'
								raise RaiseIt
							else:
								temp_string = 'NO'
					except IndexError:
						continue
	except RaiseIt:
		pass
	results.append(temp_string)

for item in results:
	print item