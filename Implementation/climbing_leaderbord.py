#!/bin/python

import sys
import bisect

n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here
database = {}	#keys are the scores, values is a list of the counter and the place in the leaderboard
place = 1
for index in xrange(len(scores)):
	if scores[index] not in database:
		database[scores[index]] = [1,place]
		place += 1
	else:
		database[scores[index]][0] += 1

scores = list(reversed(scores))

for element in alice:
	index = bisect.bisect_right(scores,element)
	#print scores, element, index
	if index == 0:
		index += 1
	if place-1 == database[scores[index-1]][1]:
		if scores[index-1] <= element:
			print place - 1
		else:
			print place
	else:
		print database[scores[index-1]][1]
