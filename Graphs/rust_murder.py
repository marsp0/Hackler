from collections import deque

tests = int(raw_input().strip())
test_database = []
for i in xrange(tests):
	n,m = [int(v) for v in raw_input().strip().split()]
	temp = {key:{} for key in xrange(1,n+1)}
	for j in xrange(m):
		a,b = [int(v) for v in raw_input().strip().split()]
		temp[a][b] = 0
		temp[b][a] = 0
	start_node = int(raw_input().strip())
	graph = {key:{} for key in xrange(1,n+1)}
	for key in temp:
		for i in xrange(1,n+1):
			if not i in temp[key] and not i in graph[key] and i != key:
				graph[key][i] = 0
				graph[i][key] = 0
	test_database.append((graph,start_node))

for test in test_database:
	graph,start_node = test
	distances = {key:0 for key in graph.keys()}
	visited = {start_node:True}
	# 1 would be white
	# 2 would be grey
	# 3 would be black
	colors = {key:1 for key in graph.keys()}
	before_list = {key:0 for key in graph.keys()}
	after_list = {}
	queue = deque([start_node])
	while queue:
		u = queue.popleft()
		for edge in graph[u]:
			if colors[edge] == 1:
				del before_list[edge]
				after_list[edge] = 0
		for key in before_list:
			colors[key] = 2
			if not key in visited:
				distances[key] = distances[u] + 1
				queue.append(key)
		colors[u] = 3
		before_list = after_list
		after_list = {}

	print distances