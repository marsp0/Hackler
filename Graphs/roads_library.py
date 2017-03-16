#!/bin/python
''' https://www.hackerrank.com/challenges/torque-and-development'''
import sys


q = int(raw_input().strip())
test_database = []
for a0 in xrange(q):
	n,m,lib,road = raw_input().strip().split(' ')
	n,m,lib,road = [int(n),int(m),int(lib),int(road)]
	graph = {key:[] for key in xrange(1,n+1)}	
	for a1 in xrange(m):
		a,b = raw_input().strip().split(' ')
		a,b = [int(a),int(b)]
		graph[a].append(b)
		graph[b].append(a)
	test_database.append(graph)

for test in test_database:
	print test