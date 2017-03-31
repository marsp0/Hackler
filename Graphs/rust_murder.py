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