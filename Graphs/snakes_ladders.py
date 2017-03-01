'''https://www.hackerrank.com/challenges/the-quickest-way-up/forum 
	
	We will be using Dijkstra (https://en.wikipedia.org/wiki/Dijkstra's_algorithm) to solve this challenge.

	Outline of what we need to do and how does the algorithm work. 

	The algorithm assigns a ''min'' distance to each vertex, this is the min distance currently processed
	that allows us to get to that vertex. By continuous relaxation we can get to the optimal path from
	the source vertex to the destination vertex.

	0. we iterate over the vertices and assign inf as the current min distance. The source has 0 as its min distance
	1. We create a min queue of all the vertices. As you can imagine the source will be the first node 
	2. We get the min node and relax all of its edges
		- check all the outgoing edges
		- if edge + node value < current assign value to the outgoing vertex
		- we update the value and bubble up the item in the queue. 
		NOTE : the hard part is to get the value in the min queue to update it.
		we will need some kind of index map to keep track of the current position of the indeces in the min queue

'''

import sys
from collections import deque

def get_name(row,col):
	return row*10+col+1

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

''' HEAP FUNCTIONS '''

def bubble_up(heap,index,index_map):
	#while the element is bigger than its parent, we continue going up
	while (index - 1)//2 >= 0 and heap[index][1] < heap[(index-1)//2][1]:
		heap[(index-1)//2], heap[index] = heap[index], heap[(index-1)//2]
		index_map[heap[(index-1)//2][0]], index_map[heap[index][0]] = index_map[heap[index][0]], index_map[heap[(index-1)//2][0]]
		index = (index-1)//2
	return index

def min_child(heap,index):
	if index*2 + 2 < len(heap):
		if heap[index][1] > heap[index*2+1][1] or heap[index][1] > heap[index*2+2][1]:
			if heap[index*2 + 1][1] < heap[index*2+2][1]:
				return index*2+1
			else:
				return index*2+2
	else:
		if heap[index][1] > heap[index*2+1][1]:
			return index*2 + 1
	return False

def bubble_down(heap,index,index_map):
	while index*2+2 <= len(heap):
		to_swap_with = min_child(heap,index)
		if to_swap_with != False:
			heap[index], heap[to_swap_with] = heap[to_swap_with], heap[index]
			index_map[heap[index][0]], index_map[heap[to_swap_with][0]] = index_map[heap[to_swap_with][0]], index_map[heap[index][0]]  
			index = to_swap_with
		else:
			break
	return index

def extract(array,index_map):
	if len(array) == 1:
		to_return = array.pop()
	else:
		to_return = array[0]
		array[0] = array.pop()
		bubble_down(heap,0,index_map)
	return to_return	

def build(array,index_map):
	size = len(array)
	for i in xrange((size)//2, -1,-1):
		bubble_down(array, i,index_map)
	return array

''' GRAPH BUILDING '''

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


for graph in database:
	predecessors = {}
	distances = []
	for vertex in graph:
		if vertex == 1:
			distances.append([1,0])
			predecessors[vertex] = vertex
		else:
			distances.append([vertex,sys.maxsize])
			predecessors[vertex] = vertex
	index_map = {distances[index][0]:index for index in xrange(len(distances))}
	distances = build(distances,index_map)
	while distances:
		node,node_distance = extract(distances,index_map)
		for edge in graph[node]:
			pass