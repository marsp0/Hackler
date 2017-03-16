#!/bin/python
''' https://www.hackerrank.com/challenges/torque-and-development'''
import sys

fish = open('test.txt','r')
q = int(fish.readline().strip())
#q = int(raw_input().strip())
test_database = []

for a0 in xrange(q):
	double_edge_counter = 0
	#n,m,lib,road = raw_input().strip().split(' ')
	#n,m,lib,road = [int(n),int(m),int(lib),int(road)]
	n,m,lib,road = [int(v) for v in fish.readline().strip().split()]
	#the graph would also contain a boolean value showing if it was visited or not
	graph = {key:[False,{}] for key in xrange(1,n+1)}	
	for a1 in xrange(m):
		#a,b = raw_input().strip().split(' ')
		#a,b = [int(a),int(b)]
		a,b = [int(v) for v in fish.readline().strip().split()]
		if not a in graph[b][1]:
			graph[a][1][b] = 1
			graph[b][1][a] = 1
	test_database.append([n,m,lib,road,graph])

def depth_first_search(start,graph,checker = None):
	stack = [start]
	counter = 0
	while stack:
		#print stack[0]
		node = stack.pop()
		graph[node][0] = True
		if checker and node in checker:
			del checker[node]
		if node != start:
			counter += 1
		for edge in graph[node][1]:
			if not graph[edge][0]:
				stack.append(edge)
				graph[edge][0] = True
	return counter

for test in test_database:
	n, m, lib, road, graph = test
	print n, m, 'lib', lib, 'road',road
	cost = 0
	roads = 0
	if road > lib or m == 0:
		print n*lib
	elif m < n:
		#if n % 2 ==0 and m % 2 == 1:
		#	print (m-1)*road + lib + (n - (m))*lib
		#else:
		print (m)*road + lib + (n - (m+1))*lib
	else:
		roads = depth_first_search(1,graph)
		cost += roads*road + lib
		not_visited = {}
		for item in graph:
			if not graph[item][0]:
				not_visited[item] = True
		while not_visited.keys():
			roads = depth_first_search(not_visited.keys()[0],graph,not_visited)
			cost += roads*road + lib
		print cost