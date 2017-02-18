''' https://www.hackerrank.com/challenges/cut-the-tree '''
''' The idea here is to use BFS and after every add of a vertex to the stack we check the difference.
	if we keep the min of the diff, after the completion the said min will be the correct one.
'''

vertices = int(raw_input().strip())
values  = [int(v) for v in raw_input().strip().split()]
edges = []
graph = {}
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

def DFS(graph):
