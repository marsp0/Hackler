import sys

n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:{} for key in xrange(1,n+1)}
edges = []
for i in xrange(m):
	a,b,w = [int(v) for v in raw_input().strip().split()]
	graph[a][b] = w
	graph[b][a] = w
	edges.append((a,b,w))

inside = [[key] for key in xrange(1,n+1)]
edges = sorted(edges, key = lambda x: x[2])
result = []
for edge in edges:
	first, second, weight = edge
	f_index = -1
	s_index = -1
	for element in xrange(len(inside)):
		if f_index == -1:
			if first in inside[element]:
				f_index = element
		if s_index == -1:
			if second in inside[element]:
				s_index = element
	if f_index != s_index:
		result.append(edge)
		inside[f_index].extend(inside[s_index])
new_graph = {key:{} for key in xrange(1,n+1)}
for item in result:
	a,b,w = item
	new_graph[a][b] = w
	new_graph[b][a] = w

stack = [1]
visited = {}
predecessor = {1:None}
while stack:
	node = stack.pop()
	visited = {1:True}
	if node == n:
		break
	for edge in new_graph[node]:
		if edge not in visited:
			stack.append(edge)
			predecessor[edge] = node

print new_graph