''' https://www.hackerrank.com/challenges/cut-the-tree '''
''' The idea here is to use BFS and after every add of a vertex to the stack we check the difference.
	if we keep the min of the diff, after the completion the said min will be the correct one.
'''
import sys
import gc
sys.setrecursionlimit(100000)
fish_filet = open('test.txt','r')
#vertices = int(raw_input().strip())
vertices = int(fish_filet.readline())
#values  = [int(v) for v in raw_input().strip().split()]
values = [int(v) for v in fish_filet.readline().strip().split()]
edges = []
graph = {}
first_child = None
second_child = None
database = {}
path = {}
for i in xrange(vertices-1):
	#inputt = (v for v in raw_input().strip().split())
	inputt = fish_filet.readline().strip().split()
	edge = [int(v) for v in inputt]
	edges.append(edge)

for i in xrange(1,vertices+1):
	graph[i] = (values[i-1],[])
for edge in edges:
	first, second = edge
	graph[first][1].append(second)
	graph[second][1].append(first)
	if first == 1:
		if first_child == None:
			first_child = second
		else:
			second_child = second
	elif second == 1:
		if first_child == None:
			first_child = first
		else:
			second_child = first

def get_sum(graph,start,parent):
	global database
	global path
	summ = graph[start][0]
	for child in graph[start][1]:
		try:
			path[child]
		except KeyError:
			if child != parent:
				path[child] = 0
				summ += get_sum(graph,child,start)
	database[start] = summ
	return summ

def DFS(graph,start):
	print '21321321'
	min_sum = sys.maxsize
	path = {}
	global database
	total_sum = sum(values)
	stack = [start]
	while len(stack) > 0:
		node = stack.pop()
		if min_sum > abs((total_sum - database[node]) - database[node]):
			min_sum = abs((total_sum - database[node]) - database[node])
		for edge in graph[node][1]:
			try:
				path[edge]
			except KeyError:
				stack.append(edge)
				path[edge] = 0
	return min_sum

get_sum(graph,1,None)
print DFS(graph,1)