n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:[] for key in xrange(1,n+1)}
for i in xrange(m):
	a,b = [int(v) for v in raw_input().strip().split()]
	graph[b].append(a)

memo = {1:0}

def get_value(memo,graph,node):
	print 'checking if {} is in memo : {}'.format(node,node in memo)
	if node in memo:
		return memo[node]
	else:
		result = len(graph[node])
		print 'iterating over the edges'
		for edge in graph[node]:
			result += get_value(memo,graph,edge)
		memo[node] = result
		return result

get_value(memo,graph,n)
print memo