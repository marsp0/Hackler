import math

n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:[] for key in xrange(1,n+1)}
for i in xrange(m):
	a,b = [int(v) for v in raw_input().strip().split()]
	graph[a].append(b)

# The first idea here is to build a new graph from the SCCs of the old using Tarjan's algorithm. Can be found 
# here : https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm

#book keeping
index = 0
stack = []
index_database = {}
on_stack = {}

def strongly_connect(v):
	global index, on_stack, index_database
	index_database[v] = [index,index] #first is index, second is lowling or the component index
	index += 1
	stack.append(v)
	on_stack[v] = True

	for edge in graph[v]:
		if not (edge in index_database):
			strongly_connect(edge)
			index_database[v][1] = min(index_database[v][1], index_database[edge][1])
		else:
			index_database[v][1] = min(index_database[v][1], index_database[edge][1])

	if index_database[v][1] == index_database[v][0]:
		pass


for v in graph:
