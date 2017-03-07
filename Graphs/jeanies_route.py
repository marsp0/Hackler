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

n,k = [int(v) for v in raw_input().strip().split()]
citties_to_deliver = [int(v) for v in raw_input().strip().split()]
edges = []
for i in xrange(n-1):
	a,b,w = [int(v) for v in raw_input().strip().split()]
	edges.append((a,b,w))

edges = sorted(edges, key = lambda x: x[2])
union_find = UnionFind(n)
result = []
for edge in edges:
	a,b,w = edge
	if not union_find.find(a-1,b-1):
		result.append(edge)
		union_find.union(a-1,b-1)

print result