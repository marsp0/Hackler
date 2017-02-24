'''https://www.hackerrank.com/challenges/the-quickest-way-up/forum 
	
	We will be using Dijkstra to solve this challenge
'''

def get_name(row,col):
	return row*10+col

def get_permission(row,col):
	if row < 0 or row > 9 or col < 0 or col > 9:
		return False
	return row,col


graph = {}

for i in xrange(10):
	for j in xrange(10):
		vertex = get_name(i,j)
		graph[vertex] = [(i,j),[]] 

for vertex in graph:
	i,j = graph[vertex][0]
	permissions = [ get_permission(i-1,j),
					get_permission(i,j-1),
					get_permission(i,j+1),
					get_permission(i+1,j),
				]
	for item in xrange(len(permissions)):
		if permissions[item] != False:
			graph[vertex][1].append(get_name(permissions[item][0],permissions[item][1]))

tests = int(raw_input().strip())
database = [graph]*tests
for test in database:
	n = int(raw_input().strip())
	for i in xrange(n):
		a,b = [int(v) for v in raw_input().strip().split()]
		test[a].append(b)
	m = int(raw_input().strip())
	for j in xrange(m):
		a,b = [int(v) for v in raw_input().strip().split()]
		test[a].append(b)

for test in database:
	for item in test.items():
		print item