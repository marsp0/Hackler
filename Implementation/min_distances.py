#!/bin/python

'''https://www.hackerrank.com/challenges/minimum-distances'''

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
dist_dict = {}

for integer in xrange(n):
	current_number = A[integer]
	try:
		dist_dict[current_number][0].append(integer)
		if dist_dict[current_number][1] > integer- dist_dict[current_number][0][-2]:
			dist_dict[current_number][1] = integer- dist_dict[current_number][0][-2]
	except KeyError:
		dist_dict[current_number] = [[integer],sys.maxsize]

temp = sys.maxsize
for item in dist_dict.values():
	if item[1] < temp:
		temp = item[1]

print temp