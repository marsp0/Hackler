# Enter your code here. Read input from STDIN. Print output to STDOUT
N,l = map(int,raw_input().split())
graph = {key:[False,[]] for key in xrange(N)}
for i in xrange(l):
	a,b = map(int,raw_input().split())
	# Store a and b in an appropriate data structure
	graph[a][1].append(b)
	graph[b][1].append(a)


def DFS(graph,root,counter):
	stack = [root]
	while stack:
		node = stack.pop()
		if graph[node][0] == False:
			graph[node][0] = True
			counter += 1
			for child in graph[node][1]:
				if graph[child][0] == False:
					stack.append(child)
	return counter
results = []
for vertex in graph:
	temp = DFS(graph,vertex,0)
	results.append(temp)

sets = [value for value in results if value != 0]
sets = list(reversed(sets))
total = 0
'''for i in xrange(len(sets)):
	for j in xrange(i+1,len(sets)):
		total += sets[i]*sets[j]
		print total
print total
'''
memo = {}
for i in xrange(len(sets)):
	if i == 0:
		memo[0] = sets[0]
		total += sets[0]*sets[1]
	else:
		memo[i] = memo[i-1] + sets[i]
		total += memo[i]*i+1
	print total
	print memo
print sets
print total