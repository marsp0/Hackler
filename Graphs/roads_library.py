#!/bin/python
''' https://www.hackerrank.com/challenges/torque-and-development'''
import sys

#fish = open('test.txt','r')
#q = int(fish.readline().strip())
q = int(raw_input().strip())
test_database = []

for a0 in xrange(q):
	double_edge_counter = 0
	n,m,lib,road = raw_input().strip().split(' ')
	n,m,lib,road = [int(n),int(m),int(lib),int(road)]
	#n,m,lib,road = [int(v) for v in fish.readline().strip().split()]
	#the graph would also contain a boolean value showing if it was visited or not
	graph = {}	
	for a1 in xrange(m):
		a,b = raw_input().strip().split(' ')
		a,b = [int(a),int(b)]
		#a,b = [int(v) for v in fish.readline().strip().split()]
		if not a in graph:
			graph[a] = {b:1}
		else:
			graph[a][b] = 1
		if not b in graph:
			graph[b] = {a:1}
		else:
			graph[b][a] = 1
	test_database.append([n,m,lib,road,graph])

def depth_first_search(start,graph):
	stack = [start]
	counter = 0
	while stack:
		#print len(stack)
		node = stack.pop()
		try:
			edges = list(graph[node])
			del graph[node]
		except KeyError:
			continue
		if node != start:
			counter += 1
		for edge in edges:
			if edge in graph:
				stack.append(edge)
	return counter

def dfs(node,graph,visited):
	stack = [node]
	visited[node] = True
	counter = -1
	while stack:
		node = stack.pop()
		counter +=1
		for edge in graph[node]:
			if not visited[edge]:
				stack.append(edge)
				visited[edge] = True
	return counter
for test in test_database:
	n, m, lib, road, graph = test
	#print n, m, 'lib', lib, 'road',road
	cost = 0
	roads = 0
	if road > lib or m == 0:
		print n*lib
	#elif m < n:
		#if n % 2 ==0 and m % 2 == 1:
		#	print (m-1)*road + lib + (n - (m))*lib
		#else:
		#print (m)*road + lib + (n - (m+1))*lib, 'dsa'
	else:
		if m > n:
			print (n-1)*road + lib
		else:
			visited = {key:False for key in graph.keys()}
			for key in visited:
				if not visited[key]:
					roads = dfs(key,graph,visited)
					cost += roads*road + lib
			print cost + (n - len(graph))*lib 