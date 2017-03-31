<<<<<<< HEAD
import sys
from collections import deque
fish = open('test.txt','r')
#tests = int(raw_input().strip())
tests = int(fish.readline().strip())
test_database = []
for i in xrange(tests):
	#n,m = [int(v) for v in raw_input().strip().split()]
	n,m = [int(v) for v in fish.readline().strip().split()]
	graph = {key:{} for key in xrange(1,n+1)}
	for j in xrange(m):
		#a,b = [int(v) for v in raw_input().strip().split()]
		a,b = [int(v) for v in fish.readline().strip().split()]
		if a == 33498 or b == 33498:
			print a,b
		graph[a][b] = 0
		graph[b][a] = 0
	#start_node = int(raw_input().strip())
	start_node = int(fish.readline().strip())
	print start_node
	test_database.append((graph,start_node))
print len(test_database)
=======
from collections import deque


tests = int(raw_input().strip())
#fish = open('test.txt','r')
#tests = int(fish.readline().strip())
test_database = []
for i in xrange(tests):
	n,m = [int(v) for v in raw_input().strip().split()]
	#n,m = [int(v) for v in fish.readline().strip().split()]
	graph = {key:{} for key in xrange(1,n+1)}
	for j in xrange(m):
		a,b = [int(v) for v in raw_input().strip().split()]
		#a,b = [int(v) for v in fish.readline().strip().split()]
		graph[a][b] = 0
		graph[b][a] = 0
	start_node = int(raw_input().strip())
	#start_node = int(fish.readline().strip())
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
				visited[key] = True
		colors[u] = 3
		before_list = after_list
		after_list = {}
	for i in xrange(1,len(graph)+1):
		if i != start_node:
			print distances[i],
	print
>>>>>>> bfab2d1edbb664c5fc487001017b8bdfd95f43f0
