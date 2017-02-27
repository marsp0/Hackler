'''https://www.hackerrank.com/challenges/the-quickest-way-up/forum 
	
	We will be using Dijkstra to solve this challenge
'''

import sys
from collections import deque

def get_name(row,col):
	return row*10+col+1

def get_permission(row,col):
	if row < 0 or row > 9 or col < 0 or col > 9:
		return False
	return row,col

def get_graph():
	graph = {}

	for i in xrange(10):
		for j in xrange(10):
			vertex = get_name(i,j)
			graph[vertex] = [(i,j),[],None] 

	for vertex in graph:
		i,j = graph[vertex][0]
		if j < 9:
			graph[vertex][1].append(get_name(i,j+1))
		else:
			if i == 9 and j == 9:
				pass
			else:
				graph[vertex][1].append(get_name(i+1,0))
	return graph

tests = int(raw_input().strip())
database = []
for i in xrange(tests):
	temp = get_graph()
	database.append(temp)
snakes  = {}
ladders = {}
for index in xrange(tests):
	snakes[index] = []
	ladders[index] = []
	n = int(raw_input().strip())
	for i in xrange(n):
		a,b = [int(v) for v in raw_input().strip().split()]
		ladders[index].append((a,b))
	m = int(raw_input().strip())
	for j in xrange(m):
		a,b = [int(v) for v in raw_input().strip().split()]
		snakes[index].append((a,b))

for index in xrange(len(database)):
	for value in snakes[index]:
		database[index][value[0]][1].append(value[1])
	for value in ladders[index]:
		database[index][value[0]][1].append(value[1])

def get_result(graph):
	current = 99
	lista = []
	while current != None:
		lista.append(current)
		current = graph[current][2]
	lista = list(reversed(lista))
	print lista
	result = 0
	temp = 0
	for index in xrange(len(lista)):
		if index+1 < len(lista):
			if lista[index+1] - lista[index] == 1:
				temp += 1
				if temp == 6:
					result += 1
					temp = 0
			else:
				result += 1
				if temp != 0:
					result += 1
					temp = 0
	return result

for test in database:
	path = {1:0}
	graph = test
	print graph
	queue = deque([(1,None)])
	while queue:
		node, parent = queue.popleft()
		#print node,parent
		#print graph[node]
		graph[node][2] = parent
		#print graph[node]
		if node == 99:
			graph[1][2] = None
			result = get_result(graph)
		else:
			for child in graph[node][1]:
				queue.append((child,node))
				path[child] = 0
	print result