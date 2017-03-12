import math

n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:[] for key in xrange(1,n+1)}
for i in xrange(m):
	a,b = [int(v) for v in raw_input().strip().split()]
	graph[b].append(a)

memo = {1:1}

def get_value(memo,graph,node):
	if node in memo:
		return memo[node]
	else:
		result = 0
		for edge in graph[node]:
			result += get_value(memo,graph,edge)
		memo[node] = result
		return result

get_value(memo,graph,n)
print int(memo[n]%(math.pow(10,9)))