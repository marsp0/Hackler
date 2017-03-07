import sys

n, m = [int(v) for v in raw_input().strip().split()]
graph = {key:{} for key in xrange(1,n+1)}

for i in xrange(m):
	a,b,w = [int(v) for v in raw_input().strip().split()]
	graph[a][b] = w

queries = int(raw_input().strip())

result = 0
for query in xrange(queries):
	distances = {key:sys.maxsize for key in xrange(1,n+1)}
	a,b = [int(v) for v in raw_input().strip().split()]
	distances[a] = 0
	unvisited_set = set([key for key in xrange(1,n+1)])
	while unvisited_set:
		#print unvisited_set
		#print graph
		node = min(distances.items(), key = lambda x:x[1] if x[0] in unvisited_set else sys.maxsize)
		node_size = node[1]
		node = node[0]
		#print node, ' node'
		for edge in graph[node]:
			#print edge, ' edge'
			#print distances[node]
			#print graph[node][edge]
			#print distances[edge]
			if distances[node] + graph[node][edge] < distances[edge]:
				distances[edge] = distances[node] + graph[node][edge]
		if node_size == sys.maxsize:
			break
		try:
			unvisited_set.remove(node)
		except KeyError:
			break
	if distances[b] == sys.maxsize:
		print -1
	else:
		print distances[b]

