n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:{} for key in xrange(1,n+1)}
for i in xrange(m):
	a,b,w = [int(v) for v in raw_input().strip().split()]
	graph[a][b] = w
	graph[b][a] = w

distances = {key:None for key in xrange(1,n+1)}

