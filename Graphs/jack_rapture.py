import sys
#fish = open('test.txt','r')
n,m = [int(v) for v in raw_input().strip().split()]
#n,m = [int(v) for v in fish.readline().strip().split()]
graph = {key:{} for key in xrange(1,n+1)}
edges = []
for i in xrange(m):
	a,b,w = [int(v) for v in raw_input().strip().split()]
	#a,b,w = [int(v) for v in fish.readline().strip().split()]
	graph[a][b] = w
	graph[b][a] = w
	edges.append((a,b,w))

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

inside = [set([key]) for key in xrange(1,n+1)]
edges = sorted(edges, key = lambda x: x[2])
result = []
union_find = UnionFind(n)
for edge in edges:
	first, second, weight = edge
	if not union_find.find(first-1,second-1):
		result.append(edge)
		union_find.union(first-1,second-1)
#print inside
new_graph = {key:{} for key in xrange(1,n+1)}
for item in result:
	a,b,w = item
	new_graph[a][b] = w
	new_graph[b][a] = w

stack = [1]
visited = {1:True}
predecessor = {1:None}
while stack:
	node = stack.pop()
	visited[node] = True
	if node == n:
		break
	for edge in new_graph[node]:
		if edge not in visited:
			stack.append(edge)
			predecessor[edge] = node

current = []
element = n
while element != None:
	try:
		current.append(new_graph[predecessor[element]][element])
	except KeyError:
		pass
	try:
		element = predecessor[element]
	except KeyError:
		current = ['NO PATH EXISTS']
		break
print max(current)