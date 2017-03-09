n,m = [int(v) for v in raw_input().strip().split()]
edges = []

class UnionFind:
	"""https://gist.github.com/SonechkaGodovykh/18f60a3b9b3e6812c071456f61f9c5a6
	"""

	def __init__(self, n):
		self._id = list(range(n))
		self._sz = [1] * n

	def _root(self, i):
		j = i
		while (j != self._id[j]):
			self._id[j] = self._id[self._id[j]]
			j = self._id[j]
		return j

	def find(self, p, q):
		return self._root(p) == self._root(q)

	def union(self, p, q):
		i = self._root(p)
		j = self._root(q)
		if i == j:
			return
		if (self._sz[i] < self._sz[j]):
			self._id[i] = j
			self._sz[j] += self._sz[i]
		else:
			self._id[j] = i
			self._sz[i] += self._sz[j]

for i in xrange(m):
	a,b,power = [int(v) for v in raw_input().strip().split()]
	w = 1 << power
	edges.append((a,b,w))

edges = sorted(edges,key = lambda x: x[2])
union_find = UnionFind(n)
results = []
for edge in edges:
	a,b,w = edge
	if not union_find.find(a-1,b-1):
		results.append(edge)
		union_find.union(a-1,b-1)

new_graph = {key:{} for key in xrange(1,n+1)}
for edge in results:
	a,b,w = edge
	new_graph[a][b] = w
	new_graph[b][a] = w

# current idea is to bfs from evry vertex and then not check the ones that have already been checked
result = 0
distances = {}
for i in xrange(1,n+1):
	priority_q = [i]
	visited = {}
	while priority_q:
		node = priority_q.pop(0)
		if node == i:
			distances[(i,node)] = 0
		visited[node] = True
		for edge in new_graph[node]:
			if edge not in visited:
				if edge > i:
					if (i,node) in distances:
						distances[(i,edge)] = distances[(i,node)] + new_graph[node][edge]
					else:
						distances[(i,edge)] = distances[(node,i)] + new_graph[node][edge]
				priority_q.append(edge)

print bin(sum(distances.values()))[2:]