'''https://www.hackerrank.com/challenges/kruskalmstrsub'''

import sys

n, m = [int(v) for v in raw_input().strip().split()]
edges = []
inside = [[v] for v in xrange(n)]
for i in xrange(m):
	a,b,c = [int(v) for v in raw_input().strip().split()]
	edges.append((a,b,c))

def get_key(element):
	return element[2]

def find_set(lista,element):
	for item in xrange(len(lista)):
		if element in lista[item]:
			return item

def union_set(lista,first,second):
	lista[first].extend(lista[second])
	lista.pop(second)


edges = sorted(edges,None,get_key)
result = []
temp_vertices = [[key] for key in xrange(1,n+1)]
for edge in edges:
	a,b,_ = edge
	first = find_set(temp_vertices,a)
	second = find_set(temp_vertices,b)
	if first != second:
		union_set(temp_vertices,first,second)
		result.append(edge)

print sum(edge[2] for edge in result)