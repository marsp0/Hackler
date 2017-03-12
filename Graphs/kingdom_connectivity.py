n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:[] for key in xrange(1,n+1)}
for i in xrange(m):
	a,b = [int(v) for v in raw_input().strip().split()]
	graph[a].append(b)
paths = {}
def dfs(u,t):
	if u == t:
		paths[u] = 1
	else:
		if u not in paths:
			paths[u] = sum(dfs(c,t) for c in graph[u])
	return paths[u]

dfs(1,n)
print graph
print paths