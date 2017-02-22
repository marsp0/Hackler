''' https://www.hackerrank.com/challenges/cut-the-tree '''
''' The idea here is to use BFS and after every add of a vertex to the stack we check the difference.
	if we keep the min of the diff, after the completion the said min will be the correct one.
'''
import sys
import gc
sys.setrecursionlimit(100000)
#fish_filet = open('test.txt','r')
vertices = int(raw_input().strip())
#vertices = int(fish_filet.readline())
values  = [int(v) for v in raw_input().strip().split()]
#values = [int(v) for v in fish_filet.readline().strip().split()]
edges = []
graph = {}
first_child = None
second_child = None
database = {}
database_sum = {}
for i in xrange(vertices-1):
	inputt = (v for v in raw_input().strip().split())
	#inputt = fish_filet.readline().strip().split()
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
	path = {root:0}
	while stack:
		node = stack[-1]
		if len(graph[node][1]) == 1:
			database_sum[node] = graph[node][0]
			stack.pop()
		else:
			temp = []
			summ = graph[node][0]
			for index in xrange(len(graph[node][1])):
				try:
					summ += database_sum[graph[node][1][index]]
				except KeyError as e:
					temp.append(e.args[0])
					continue
			if len(temp) > 1:
				for item in temp:
					if item not in path and item != None:
						stack.append(item)
						path[item] = 0
			else:
				database_sum[node] = summ
				stack.pop()
	database_sum[1] = graph[1][0]
	for index in xrange(len(graph[1][1])):
		if graph[1][1][index] != None:
			database_sum[1] += database_sum[graph[1][1][index]]


def DFS(graph,start):
	min_sum = sys.maxsize
	path = {}
	global database_sum
	total_sum = sum(values)
	stack = [start]
	while len(stack) > 0:
		node = stack.pop()
		if node != None:
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
get_sum(graph,1)
print DFS(graph,1)