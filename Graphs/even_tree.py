'''https://www.hackerrank.com/challenges/even-tree'''

n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:[] for key in xrange(1,n+1)}
for i in xrange(m):
	a,b = [int(v) for v in raw_input().strip().split()]
	graph[a].append(b)
	graph[b].append(a)
database = {}
def get_sum(graph,root):
	stack = [root]
	path = {root:0}
	while stack:
		node = stack[-1]
		if len(graph[node]) == 1:
			database[node] = 1
			path[node] = 0
			stack.pop()
		else:
			track_errors = []
			temp = 1
			for child in graph[node]:
				try:
					temp += database[child]
				except KeyError as e:
					track_errors.append(e.args[0])
					continue
			if len(track_errors) > 1:
				for item in track_errors:
					if item not in path:
						stack.append(item)
						path[item] = 0
			else:
				database[node] = temp
				stack.pop()
	database[1] = 1 + sum([database[child] for child in graph[1]])

get_sum(graph,1)
edges = 0
for item in database:
	if item != 1 and database[item] % 2 == 0:
		edges += 1
print edges