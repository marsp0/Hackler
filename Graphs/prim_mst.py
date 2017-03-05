import sys

n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:{} for key in xrange(1,n+1)}
for index in xrange(m):
	a,b,w = [int(v) for v in raw_input().strip().split()]
	if b in graph[a]:
		if graph[a][b] > w:
			graph[a][b] = w
			graph[b][a] = w
	else:
		graph[b][a] = w
		graph[a][b] = w
start_node = int(raw_input().strip())

min_values = {key:[None,sys.maxsize] for key in xrange(1,n+1)}
min_values[start_node] = [None,0]
result = 0
while min_values:
	node = min(min_values.items(), key = lambda x: x[1][1])
	del min_values[node[0]]
	#print node, ' is current'
	result += node[1][1]
	for edge in graph[node[0]]:
		#print ' considering ',edge
		if edge in min_values:
			if graph[node[0]][edge] < min_values[edge][1]:
				#print min_values
				#print 'replacing ',edge
				#print 'new is ', graph[node[0]][edge], ' old is ', min_values[edge]
				min_values[edge] = [edge,graph[node[0]][edge]]

print result