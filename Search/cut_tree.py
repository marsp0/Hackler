''' https://www.hackerrank.com/challenges/cut-the-tree '''
''' The idea here is to use BFS and after every add of a vertex to the stack we check the difference.
	if we keep the min of the diff, after the completion the said min will be the correct one.
'''
import sys

vertices = int(raw_input().strip())
values  = [int(v) for v in raw_input().strip().split()]
edges = []
graph = {}
first_child = None
second_child = None
for i in xrange(vertices-1):
	inputt = raw_input().strip().split()
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

def DFS(graph,start):
	min_sum = sys.maxsize
	current_sum = 0
	global values
	total_sum = sum(values)
	stack = [start]
	visited = {}
	path = []
	while len(stack) > 0:
		node = stack.pop()
		try:
			visited[node]
		except KeyError:
			visited[node] = 0
			current_sum += graph[node][0]
			total_sum -= graph[node][0]
			if min_sum > abs(total_sum - current_sum):
				min_sum = abs(total_sum - current_sum)
			for edge in graph[node][1]:
				stack.append(edge)
			temp = node
			path.append(temp)
	print path
	return min_sum



print DFS(graph,1)