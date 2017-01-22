#!/bin/python

''' https://www.hackerrank.com/challenges/acm-icpc-team'''

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)

teams = {}
for i in xrange(n):
	for j in xrange(i+1,n):
		teams[(i,j)] = 0
		first = int(topic[i],2)
		second = int(topic[j],2)
		teams[(i,j)] += bin(first | second).count('1')

result = [((0,1),teams[(0,1)])]
current_max = teams[0,1]
for team in teams:
	if teams[team] > current_max:
		result = [(team,teams[team])]
		current_max = teams[team]
	elif teams[team] == current_max:
		result.append((team,teams[team]))

print result[0][1]
print len(result)
