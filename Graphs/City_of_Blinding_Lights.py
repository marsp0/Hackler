import sys

#UPDATE > The test cases timed out even with a HEAP. HOLY SHIT

''' HEAP FUNCTIONS '''
def bubble_up(heap,index,index_map):
	#while the element is bigger than its parent, we continue going up
	while (index - 1)//2 >= 0 and heap[index][1] < heap[(index-1)//2][1]:
		heap[(index-1)//2], heap[index] = heap[index], heap[(index-1)//2]
		index_map[heap[(index-1)//2][0]], index_map[heap[index][0]] = index_map[heap[index][0]], index_map[heap[(index-1)//2][0]]
		index = (index-1)//2
	return index

def min_child(heap,index):
	if index*2 + 2 < len(heap):
		if heap[index][1] > heap[index*2+1][1] or heap[index][1] > heap[index*2+2][1]:
			if heap[index*2 + 1][1] < heap[index*2+2][1]:
				return index*2+1
			else:
				return index*2+2
	else:
		if heap[index][1] > heap[index*2+1][1]:
			return index*2 + 1
	return False

def bubble_down(heap,index,index_map):
	while index*2+2 <= len(heap):
		to_swap_with = min_child(heap,index)
		if to_swap_with != False:
			heap[index], heap[to_swap_with] = heap[to_swap_with], heap[index]
			index_map[heap[index][0]], index_map[heap[to_swap_with][0]] = index_map[heap[to_swap_with][0]], index_map[heap[index][0]]  
			index = to_swap_with
		else:
			break
	return index

def extract(array,index_map):
	if len(array) == 1:
		to_return = array.pop()
	else:
		to_return = array[0]
		array[0] = array.pop()
		index_map[array[0][0]] = 0
		bubble_down(array,0,index_map)
	return to_return	

def build(array,index_map):
	size = len(array)
	for i in xrange((size)//2, -1,-1):
		bubble_down(array, i,index_map)
	return array

''' END OF HEAP '''

n, m = [int(v) for v in raw_input().strip().split()]
#fish = open('test.txt', 'r')
#n, m = [int(v) for v in fish.readline().strip().split()]
graph = {key:{} for key in xrange(1,n+1)}

for i in xrange(m):
	a,b,w = [int(v) for v in raw_input().strip().split()]
	#a,b,w = [int(v) for v in fish.readline().strip().split()]
	graph[a][b] = w

queries = int(raw_input().strip())
#queries = int(fish.readline().strip())

result = []
database = {} 
for query in xrange(queries):
	distances = {key:sys.maxsize for key in xrange(1,n+1)}
	a,b = [int(v) for v in raw_input().strip().split()]
	#a,b = [int(v) for v in fish.readline().strip().split()]
	if (a,b) not in database:
		distances[a] = 0
		heap = [[key, distances[key]] for key in xrange(1,n+1)]
		index_map = {key:key-1 for key in xrange(1,n+1)}
		heap = build(heap, index_map)
		while heap:
			node, node_size = extract(heap,index_map)
			for edge in graph[node]:
				if distances[node] + graph[node][edge] < distances[edge]:
					distances[edge] = distances[node] + graph[node][edge]
					heap[index_map[edge]][1] = distances[node] + graph[node][edge]
					bubble_up(heap,index_map[edge], index_map)
		if distances[b] == sys.maxsize:
			result.append(-1)
		else:
			result.append(distances[b])
		database[(a,b)] = result[-1]
	else:
		result.append(database[(a,b)])

for item in result:
	print item