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
	graph = {}	
	for a1 in xrange(m):
		#a,b = raw_input().strip().split(' ')
		#a,b = [int(a),int(b)]
		a,b = [int(v) for v in fish.readline().strip().split()]
		if not a in graph:
			graph[a] = {b:1}
		else:
			graph[a][b] = 1
		if not b in graph:
			graph[b] = {a:1}
		else:
			graph[b][a] = 1

	print len(graph)
	test_database.append([n,m,lib,road,graph])

def depth_first_search(start,graph):
	stack = [start]
	counter = 0
	while stack:
		#print len(stack)
		node = stack.pop()a
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

for test in test_database:
	n, m, lib, road, graph = test
	print n, m, 'lib', lib, 'road',road
	cost = 0
	roads = 0
	if road > lib or m == 0:
		print n*lib
	#elif m < n:
		#if n % 2 ==0 and m % 2 == 1:
		#	print (m-1)*road + lib + (n - (m))*lib
		#else:
		#print (m-1)*road + lib + (n - (m))*lib
	else:
		roads = depth_first_search(1,graph)
		#if roads > 0 :
			#print roads, 'first iteration'
		cost += roads*road + lib
		while graph.keys():
			roads = depth_first_search(graph.keys()[0],graph)
			#if roads > 0 :
			#	print roads, 'next iterations'
			cost += roads*road + lib
		print cost

#5179530931