'''https://www.hackerrank.com/challenges/dijkstrashortreach'''

import sys

#fish = open('test.txt', 'r')
tests = int(raw_input().strip())
#tests = int(fish.readline().strip())
def key(dicta,item):
	return dicta[item]

for test in xrange(tests):
	n,m = [int(v) for v in raw_input().strip().split()]
	#n,m = [int(v) for v in fish.readline().strip().split()]
	graph = {key:{} for key in xrange(1,n+1)}
	distances = {key:sys.maxsize for key in xrange(1,n+1)}
	predecessors = {key:key for key in xrange(1,n+1)}
	temp = None
	for i in xrange(m):
		a,b,w = [int(v) for v in raw_input().strip().split()]
		#a,b,w = [int(v) for v in fish.readline().strip().split()]
		if b in graph[a]:
			if graph[a][b] > w:
				graph[a][b] = w
				graph[b][a] = w
		else:
			graph[a][b] = w
			graph[b][a] = w
	start_node = int(raw_input().strip())
	#start_node = int(fish.readline().strip())
	distances[start_node] = 0
	unvisited_set = set(graph.keys())
	current = start_node
	unvisited_set.remove(start_node)
	while unvisited_set:
		for edge in graph[current]:
			if distances[current] + graph[current][edge] < distances[edge]:
				distances[edge] = distances[current] + graph[current][edge]
				predecessors[edge] = current
		current = min(distances.items(), key = lambda x: x[1] if x[0] in unvisited_set else sys.maxsize)
		if current[1] == sys.maxsize:
			break
		else:
			current = current[0]
		try:
			unvisited_set.remove(current)
		except KeyError:
			break
	for item in distances:
		if item != start_node:
			if distances[item] == sys.maxsize:
				print -1,
			else:
				print distances[item],
		print