import sys
from collections import deque
def insert(graph,a,b):
	index_list = [x for x in xrange(a-6,a) if x >= 1]
	for item in index_list:
		try:
			index = graph[item].index(a)
			graph[item][index] = b
		except ValueError:
			continue
	graph[a] = [b]

tests = int(raw_input())
test_database = []
for i in xrange(tests):
	graph = {key:[x for x in xrange(key+1,key+7) if x <= 100] for key in xrange(1,101)}
	ladders = int(raw_input().strip())
	for x in xrange(ladders):
		a,b = [int(v) for v in raw_input().strip().split()]
		insert(graph,a,b)
	snakes = int(raw_input().strip())
	for x in xrange(snakes):
		a,b = [int(v) for v in raw_input().strip().split()]
		insert(graph,a,b)
	test_database.append(graph)


for test in test_database:
	graph = test
	parents = {key:None for key in xrange(1,101)}
	queue = deque([(1,1)])
	visited = {1:True}
	while queue:
		node, parent = queue.popleft()
		parents[node] = parent
		if node == 100:
			break
		for edge in graph[node]:
			if edge not in visited:
				queue.append((edge,node))
				visited[edge] = True
	key = 100
	counter = 0
	try:
		while key != parents[key]:
			counter += 1
			key = parents[key]
	except KeyError:
		counter = -1
	print counter