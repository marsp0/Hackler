#!/bin/python
''' https://www.hackerrank.com/challenges/torque-and-development'''
import sys

fish = open('test.txt','r')
q = int(fish.readline().strip())
#q = int(raw_input().strip())
test_database = []
for a0 in xrange(q):
	#n,m,lib,road = raw_input().strip().split(' ')
	#n,m,lib,road = [int(n),int(m),int(lib),int(road)]
	n,m,lib,road = [int(v) for v in fish.readline().strip().split()]
	#the graph would also contain a boolean value showing if it was visited or not
	graph = {key:[False,[]] for key in xrange(1,n+1)}	
	for a1 in xrange(m):
		#a,b = raw_input().strip().split(' ')
		#a,b = [int(a),int(b)]
		a,b = [int(v) for v in fish.readline().strip().split()]
		graph[a][1].append(b)
		graph[b][1].append(a)
	test_database.append([n,m,lib,road,graph])

def depth_first_search(start,graph,checker = None):
	#stack to keep track of the nodes that have to be processed
	stack = [start]
	#the counter variable will be used just to give me an indication of the number of edges needed
	#for the minimum spanning tree
	counter = 0
	while stack:
		node = stack.pop()
		graph[node][0] = True
		if checker and node in checker:
			del checker[node]
		if node != start:
			counter += 1
		for edge in graph[node][1]:
			#if we have seen the edge before, we don't need to process it again
			#we could, but it would just create a cycle that we don't need 
			if not graph[edge][0]:
				stack.append(edge)
				graph[edge][0] = True
	return counter

for test in test_database:
	n, m, lib, road, graph = test
	print n,m,lib,road
	cost = 0
	roads = 0
	#the logic here
	#a road connects two cities and if the cost of two libraries
	# is smaller than the cost of one road, then we can just build n libraries
	if road > 2*lib or m == 0:
		print n*lib
	else:
		#Q: what would DFS give us ?
		#A: get a list of edges that connect the whole city and it should be acyclic graph.
		# Since this is an undirected graph it would give us an minimum spanning tree (although every
		#	tree in this graph is a minimum spanning tree)
		#Q: Where should we start the DFS from ?
		#A: Try with 1 and if we see an untouched vertices afterwards, just start with the first 

		#this line takes care only of the cities connected to one, but they might be disconnected
		roads = depth_first_search(1,graph)
		#print 'first iteration roads are {}'.format(roads)
		cost += roads*road + lib
		not_visited = {}
		for item in graph:
			if not graph[item][0]:
				not_visited[item] = True
		while not_visited.keys():
			roads = depth_first_search(not_visited.keys()[0],graph,not_visited)
			cost += roads*road + lib
			#print 'next iteration roads are {}'.format(roads)
		print cost