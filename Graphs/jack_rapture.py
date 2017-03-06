import sys

n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:{} for key in xrange(1,n+1)}
for i in xrange(m):
	a,b,w = [int(v) for v in raw_input().strip().split()]
	graph[a][b] = w
	graph[b][a] = w

distances = {key:sys.maxsize for key in xrange(1,n+1)}
distances[1] = 0
predecessors = {key:None for key in xrange(1,n+1)}
seen = {key:False for key in xrange(1,n+1)}
def get_sum(predecessors, element):
	temp = 0
	while element != None:
		#print 'element is ', element, distances[element]
		#print predecessors
		temp += distances[element]
		element = predecessors[element]
	return temp

vertices = {key:True for key in xrange(1,n+1)}

while vertices:
	node = min(distances.items(), key = lambda x: x[1] if x[0] in vertices else sys.maxsize)[0]
	del vertices[node]
	seen[node] = True
	print distances
	if node != sys.maxsize:
		for edge in graph[node]:
			if not seen[edge]:
				prev_distances = get_sum(predecessors,node)
				print node, edge, graph[node][edge], prev_distances
				if graph[node][edge] - prev_distances < distances[edge]:
					if graph[node][edge] - prev_distances < 0:
						distances[edge] = 0
					else:
						distances[edge] = graph[node][edge] - prev_distances
					print node, edge
					predecessors[edge] = node
	else:
		break
print distances