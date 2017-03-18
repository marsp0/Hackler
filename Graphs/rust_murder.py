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
	