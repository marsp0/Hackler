'''https://www.hackerrank.com/challenges/johnland'''

#fish = open('test.txt','r')
#n,m = [int(v) for v in fish.readline().strip().split()]
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
	#a,b,power = [int(v) for v in fish.readline().strip().split()]
	edges.append((a,b,power))

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

#IDEA TAKEN FROM THE DISCUSSION FORUM : Use DFS from a certain node (just 1, so its already better than the previous)
#and keep track of how many children (self included) each vertex has. The amount of times an edge is used
# is equal to (n-num_children)*num_children
stack = [1]
child_number = {}
visited = {}
inside = {1:True}
print new_graph
while stack:
	node = stack[-1]
	if len(new_graph[node]) == 1 and node != 1:
		child_number[node] = 1
		visited[node] = True
		stack.pop()
	else:
		temp = []
		result = 1
		for edge in new_graph[node]:
			try:
				result += child_number[edge]
			except KeyError:
				temp.append(edge)
		if len(temp) <= 1:
			if node != 1:
				child_number[node] = result
				visited[node] = True
				stack.pop()
			else:
				result = 1
				temp_1 = 0
				for edge in new_graph[1]:
					try:
						result += child_number[edge]
					except KeyError:
						temp_1 += 1
						break
				if temp_1 == 0:
					child_number[1] = result
					stack.pop()
					temp = []
		for edge in temp:
			if not edge in inside:
				stack.append(edge)
				inside[edge] = True
result = 0
for vertex in new_graph:
	for edge in new_graph[vertex]:
		if child_number[vertex] < child_number[edge]:
			main = child_number[vertex]
		else:
			main = child_number[edge]
		result += (1<<new_graph[vertex][edge])*(n-main)*main
print bin(result/2)[2:]