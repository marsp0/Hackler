'''https://www.hackerrank.com/challenges/the-quickest-way-up/forum 
	
	We will be using Dijkstra to solve this challenge
'''

import sys
from collections import deque

def get_name(row,col):
	return row*10+col

def get_permission(row,col):
	if row < 0 or row > 9 or col < 0 or col > 9:
		return False
	return row,col

graph = {}

for i in xrange(10):
	for j in xrange(10):
		vertex = get_name(i,j)
		graph[vertex] = [(i,j),[],None] 

for vertex in graph:
	i,j = graph[vertex][0]
	permissions = [ get_permission(i-1,j),
					get_permission(i,j-1),
					get_permission(i,j+1),
					get_permission(i+1,j),
				]
	for item in xrange(len(permissions)):
		if permissions[item] != False:
			graph[vertex][1].append(get_name(permissions[item][0],permissions[item][1]))

tests = int(raw_input().strip())
database = [graph]*tests
for test in database:
	n = int(raw_input().strip())
	for i in xrange(n):
		a,b = [int(v) for v in raw_input().strip().split()]
		test[a][1].append(b)
	m = int(raw_input().strip())
	for j in xrange(m):
		a,b = [int(v) for v in raw_input().strip().split()]
		test[a][1].append(b)

def get_result(graph):
	current = 99
	temp = 0
	while current != None:
		temp += 1
		print graph[current][2]
		current = graph[current][2]
	return temp

for test in database:
	path = {}
	graph = test
	queue = deque([(0,None)])
	while queue:
		node, parent = queue.popleft()
		#print graph[node]
		graph[node][2] = parent
		#print graph[node]
		if node == 99:
			graph[0][2] = None
			result = get_result(graph)
		else:
			for child in graph[node][1]:
				if child not in path:
					queue.append((child,node))
					path[child] = 0
	print result