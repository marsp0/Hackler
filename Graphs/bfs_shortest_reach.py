'''https://www.hackerrank.com/challenges/bfsshortreach'''

from collections import deque
import sys

q = int(raw_input().strip())
database = []
for i in xrange(q):
	n,m = [int(v) for v in raw_input().strip().split()]
	graph = {key:[] for key in xrange(1,n+1)}
	for j in xrange(m):
		a,b = [int(v) for v in raw_input().strip().split()]
		if b not in graph[a]:
			graph[a].append(b)
		if a not in graph[b]:
			graph[b].append(a)
	start = int(raw_input().strip())
	database.append((start,graph))

def BFS(graph,start):
	queue = deque([start])
	path_len = {start:0}
	while queue:
		node = queue.popleft()
		for child in graph[node]:
			if child in path_len:
				try:
					if path_len[child] + 1 < path_len[node]:
						path_len[node] = path_len[child] + 1
				except KeyError:
					path_len[node] = path_len[child]+ 1
			else:
				queue.append(child)
	return path_len

for test in database:
	start, graph = test
	#for item in graph:
	#	print item, graph[item]
	results = BFS(graph,start)
	temp = []
	for index in xrange(1,len(graph)+1):
		if index != start:
			try:
				temp.append(results[index]*6)
			except KeyError:
				temp.append(-1)
	for item in temp:
		print item,
	print

