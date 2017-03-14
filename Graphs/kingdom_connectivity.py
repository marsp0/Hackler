import math
import copy

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

#what do we need to do now
# Q. Figure out how to construct the new graph G' and what info is going in it (how do we represent SCC)
#
# A: iterate over the keys of the index_database and let the first new SCC be the root.
# 		Every other element from the same SCC will just increment a counter, this way
#		we can check afterwards if the given G' vertex is a cycle or not.
#
# Q. How do we check if an SCC identifier has already been inserted in the graph ?
# A: Using a hash table to keep track of the already used identifiers
#

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
		#the counter to check for cycles and the list for the outgoing edges
		scc_graph[v] = [1,[]]

# what we did here is the following: 
# 1. in the previous iteration over the vertices of the index_database we were falling in the situation
#		where we want to add edge to a non existent SCC
# 2. Instead of saving them in a temp array we can just not add them. The extra array would create a mess
# 3. We run another iteration over the values and now all the SCCs are created so no issues
#

scc_graph_forward = copy.deepcopy(scc_graph)  #will keep the graph with the forward edges. A -> B is under scc_graph_forward[A]
for value in index_database.values():
	for edge in value[1]:
		root = already_in_scc[value[0][1]]
		if index_database[edge][0][1] != value[0][1]:
			try:
				scc_graph[edge][1].append(root)
				scc_graph_forward[root][1].append(edge)
			except KeyError:
				edge = already_in_scc[index_database[edge][0][1]]
				scc_graph[edge][1].append(root)
# The idea now is to use another DFS with memoization
memo = {1:1}	#dict for the amount of ways to get to that node
def get_value(memo,graph,node):
	if node in memo:
		return memo[node]
	else:
		result = 0
		for edge in graph[node][1]:		#[1] because the first element is the SCC counter
			result += get_value(memo,graph,edge)
		memo[node] = result
		return result

# This is for step 2
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
	get_value(memo,scc_graph,n)
	print int(memo[n] % (math.pow(10,9)))
else:
	print result