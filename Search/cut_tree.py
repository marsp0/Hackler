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
database_sum = {}
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

def get_sum(graph,root):
	stack = [root]
	path = {}
	while stack:
		print stack
		print graph[1]
		print graph[27053]
		print graph[2900]
		print graph[38169]
		print graph[83233]
		print graph[66738]
		print graph[41676]
		print graph[9147]
		print graph[69077]
		print
		print 
		node = stack[-1]
		if len(graph[node][1]) == 1:
			database_sum[node] = graph[node][0]
			stack.pop()
		else:
			try:
				summ = graph[node][0]
				for index in xrange(1,len(graph[node][1])):
					summ += database_sum[graph[node][1][index]]
				database_sum[node] = summ
				stack.pop()
			except KeyError:
				for index in xrange(1,len(graph[node][1])):
					child = graph[node][1][index]
					if child not in database_sum and child not in path:
							stack.append(child)
							path[child] = 0
	database_sum[1] = graph[1][0]
	for index in xrange(len(graph[1][1][1:])):
		database_sum[1] += database_sum[graph[1][1][index]]


def DFS(graph,start):
	min_sum = sys.maxsize
	path = {}
	global database_sum
	total_sum = sum(values)
	stack = [start]
	while len(stack) > 0:
		node = stack.pop()
		if min_sum > abs((total_sum - database_sum[node]) - database_sum[node]):
			min_sum = abs((total_sum - database_sum[node]) - database_sum[node])
		for edge in graph[node][1]:
			try:
				path[edge]
			except KeyError:
				stack.append(edge)
				path[edge] = 0
	return min_sum
graph[1][1].insert(0,None)
print get_sum(graph,1)

print database_sum