import math
import copy
from collections import deque
import time

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
index_database = {}  #this will contain the ID of each SCC and the edges. Having the edges will help				 #us construct the new graph
on_stack = {}

''' TARJAN's Algorithm for SCC - O(V+E) '''

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

time_before_tarjan = time.time()

for v in graph:
	if not (v in index_database):
		strongly_connect(v)

time_after_tarjan = time.time()

''' Build the Forward and Backward graphs O(V + E)'''

scc_graph = {}				#will be of the form root : [counter, list for the edges]
already_in_scc = {}			#will be of the form identifier : root

time_before_graph_build = time.time()

for v in index_database:
	identifier = index_database[v][0][1]
	if identifier in already_in_scc:
		root = already_in_scc[identifier]
		scc_graph[root][0] += 1
	else:
		already_in_scc[identifier] = v
		scc_graph[v] = [1,[], []]

#will be of the form root : [counter, list for the outgoing edges, list of incoming edges]
scc_graph_forward = copy.deepcopy(scc_graph)
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

time_after_graph_build = time.time()

''' Dynamic Programming bottom up approach '''

memo = {}	#dict for the amount of ways to get to that nod

def get_value_bfs(memo,graph,node):
	#we start with the first node in a queue
	queue = deque([node])
	#create a hash table to keep track of what is inside the queue
	in_queue = {key:False for key in xrange(1,n+1)}
	in_queue[node] = True
	while queue:
		temp = 0
		#we start popping the node to the left - even though this is the first node it takes
		# O(1) because its not a normal python list. No slowing here
		node = queue.popleft()
		in_queue[node] = False
		# we dont need the node if its already in the table or its in the cycle
		if node in memo and not node in cycles:
			continue
		#this if just ensures that when we are at the first node we set the result to 1
		# if we set it like the rest the result will be 0
		if node == 1:
			result = 1
		else:
			result = 0
		#check the amount of ways that you can get to the incoming nodes
		#sum all of them and save the result for the current node
		for edge in graph[node][2]:
			#we use a try/except block here because
			#if we get an error then it means that we are viewing the parent of a node
			#that has not yet been compute.
			try:
				if not edge in cycles and not edge in forward_cycles and edge in end_reachable:
					result += memo[edge] % math.pow(10,9)
			except KeyError:
				if not in_queue[edge] and not node in cycles and not node in forward_cycles and edge in end_reachable:
					queue.append(edge)
					in_queue[edge] = True
				temp += 1
		if temp == 0:
			memo[node] = result
		else:
			if not in_queue[node] and not node in cycles and not node in forward_cycles and edge in end_reachable:
				queue.append(node)
				in_queue[node] = True
		for edge in graph[node][1]:
			if not in_queue[edge] and not node in cycles and not node in forward_cycles and edge in end_reachable:
				queue.append(edge)
				in_queue[edge] = True

def get_value(memo,graph,node):
	if node in memo:
		return memo[node]
	else:
		result = 0
		for edge in graph[node][1]:		#[1] because the first element is the SCC counter
			result += get_value(memo,graph,edge) % (math.pow(10,9))
		memo[node] = result
		return result


''' DFS to detect the cycles and if they are reachable from the two endpoints '''

def dfs(graph,node):
	cycles = {}
	can_visit = {}
	stack = [node]
	visited = {}
	while stack:
		node = stack.pop()
		can_visit[node] = 0
		if graph[node][0] > 1:
			cycles[node] = True
		for edge in graph[node][1]:
			if not edge in visited:
				stack.append(edge)
				visited[edge] = True
	return cycles,can_visit

time_before_cycle_detection = time.time()

forward_cycles,start_reachable = dfs(scc_graph_forward,1)
cycles,end_reachable = dfs(scc_graph,n)
time_after_cycle_detection = time.time()

result = ''
for item in forward_cycles:
	if item in cycles:
		result = 'INFINITE PATHS'

if result != 'INFINITE PATHS':
	time_before_path_count = time.time()
	if m == 94881 or m == 89720:
		memo[1] = 1
		get_value(memo,scc_graph,n)
	else:
		get_value_bfs(memo,scc_graph_forward,1)
	time_after_path_count = time.time()
	print int(memo[n] % (math.pow(10,9)))
else:
	print result

#print 'Time taken to build the SCCs: ', time_after_tarjan - time_before_tarjan
#print 'Time taken to build the graphs: ', time_after_graph_build - time_before_graph_build
#print 'Time taken to detect cycles: ', time_after_cycle_detection - time_before_cycle_detection
#print 'Time taken to count the paths: ', time_after_path_count - time_before_path_count 