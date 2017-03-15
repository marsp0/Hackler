import math
import copy
from collections import deque

''' Challenge link : https://www.hackerrank.com/challenges/kingdom-connectivity'''

n,m = [int(v) for v in raw_input().strip().split()]
graph = {key:[] for key in xrange(1,n+1)}
for i in xrange(m):
	a,b = [int(v) for v in raw_input().strip().split()]
	graph[a].append(b)

# The first idea here is to build a new graph from the SCCs of the old using Tarjan's algorithm. Can be found 
# here : https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm

#book keeping
index = 0
stack = []
index_database = {}  #this will contain the ID of each SCC and the edges. Having the edges will help
					 #us construct the new graph
on_stack = {}

def strongly_connect(v):
	''' modified version of DFS '''
	global index, on_stack, index_database
	index_database[v] = ([index,index], []) #first is index, second is lowling or the component index
	index += 1
	stack.append(v)
	on_stack[v] = True

	for edge in graph[v]:
		if not (edge in index_database):
			strongly_connect(edge)
			index_database[v][0][1] = min(index_database[v][0][1], index_database[edge][0][1])
		elif edge in on_stack and on_stack[edge]:
			index_database[v][0][1] = min(index_database[v][0][1], index_database[edge][0][1])
		index_database[v][1].append(edge)

	if index_database[v][0][0] == index_database[v][0][1]:
		w = None
		while w != v:
			w = stack.pop()
			on_stack[w] = False

for v in graph:
	if not (v in index_database):
		strongly_connect(v)

def get_scc_root(node):
	return already_in_scc[node]

scc_graph = {}				#will be of the form root : [counter, list for the edges]
already_in_scc = {}			#will be of the form identifier : root

for v in index_database:
	identifier = index_database[v][0][1]
	if identifier in already_in_scc:
		root = already_in_scc[identifier]
		scc_graph[root][0] += 1
	else:
		already_in_scc[identifier] = v
		scc_graph[v] = [1,[], []]


scc_graph_forward = copy.deepcopy(scc_graph)  #will keep the graph with the forward edges. A -> B is under scc_graph_forward[A]
for value in index_database.values():
	for edge in value[1]:
		root = already_in_scc[value[0][1]]
		if index_database[edge][0][1] != value[0][1]:
			try:
				scc_graph[edge][1].append(root)
				scc_graph_forward[root][1].append(edge)
				scc_graph_forward[edge][2].append(root)
			except KeyError:
				edge = already_in_scc[index_database[edge][0][1]]
				scc_graph[edge][1].append(root)
				scc_graph_forward[edge][2].append(root)
# The idea now is to use another DFS with memoization
memo = {}	#dict for the amount of ways to get to that node

# This needs to happen in bottom up
def get_value(memo,graph,node):
	if node in memo:
		return memo[node]
	else:
		result = 0
		for edge in graph[node][1]:		#[1] because the first element is the SCC counter
			result += (get_value(memo,graph,edge) % math.pow(10,9))
		memo[node] = result
		return result

def get_value_bfs(memo,graph,node):
	queue = deque([node])
	in_queue = {key:False for key in xrange(1,n+1)}
	in_queue[node] = True
	while queue:
		if len(memo) == 2501:
			return False
		temp = 0
		node = queue.popleft()
		in_queue[node] = False
		if node in memo:
			continue
		if node == 1:
			result = 1
		else:
			result = 0
		for edge in graph[node][2]:		#[1] because the first element is the SCC counter
			try:
				result += memo[edge] % math.pow(10,9)
			except KeyError:
				if not in_queue[edge]:
					queue.append(edge)
					in_queue[edge] = True
				temp += 1
				break
		if temp == 0:
			memo[node] = result
		else:
			if not in_queue[node]:
				queue.append(node)
				in_queue[node] = True
		for edge in graph[node][1]:
			if not in_queue[edge]:
				queue.append(edge)
				in_queue[edge] = True


cycles = {}		#a dict to save the vertices that represent cycles

stack = [n]
visited = {} 	#NOTE :do we really nead it ?
while stack:
	node = stack.pop()
	if scc_graph[node][0] > 1:
		cycles[node] = True
	for edge in scc_graph[node][1]:
		if edge not in visited:
			stack.append(edge)
			visited[edge] = True

forward_cycles = {}
stack = [1]
visited = {} 	#NOTE :do we really nead it ?
while stack:
	node = stack.pop()
	if scc_graph_forward[node][0] > 1:
		forward_cycles[node] = True
	for edge in scc_graph_forward[node][1]:
		if edge not in visited:
			stack.append(edge)
			visited[edge] = True

result = ''
for item in forward_cycles:
	if item in cycles:
		result = 'INFINITE PATHS'

if result != 'INFINITE PATHS':
	p = get_value_bfs(memo,scc_graph_forward,1)
	if p != None:
		get_value(memo,scc_graph,n)
	print int(memo[n] % (math.pow(10,9)))
else:
	print result