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
			stack.pop()
		else:
			track_errors = []
			temp = 0
			try:
				for child in graph[node]:
					database[child]
					temp += 1
					stack.append(child)
			except KeyError as e:
				track_errors.append(e.args[0])
			if track_errors > 1:
				for item in track_errors:



print get_sum(graph,1)
print database