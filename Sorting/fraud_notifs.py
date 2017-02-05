from math import ceil
import heapq as hq
n, d = raw_input().strip().split()
n,d = int(n), int(d)
array = [int(v) for v in raw_input().strip().split()]
#array = [int(v) for v in open('test.txt','r').read().strip().split()]
array[:d] = sorted(array[:d])
notifs = 0
if d % 2 == 0:
	max_heap = array[:d/2+1]
	hq._heapify_max(max_heap)

	min_heap = array[d/2+1:d]
	hq.heapify(min_heap)
else:
	max_heap = array[:d/2+1]
	hq._heapify_max(max_heap)
	min_heap = array[d/2+1:d]
	hq.heapify(min_heap)

for i in xrange(d,n):
	#we need to check if notifs gets aumented
	if d%2==1:
		median = max_heap[0]
	else:
		median = (max_heap[0] + max_heap[1])/2
	if 2*median <= array[i]:
		notifs += 1

	if array[i-d] <= max_heap[0]:
		print max_heap, min_heap, array[i]
		to_remove = max_heap.index(array[i-d])
		max_heap[-1], max_heap[to_remove] = max_heap[to_remove], max_heap[-1]
		temp = max_heap[to_remove:-1]
		hq._heapify_max(temp)
		max_heap.pop(0)
		max_heap[to_remove:] = temp
	else:
		to_remove = min_heap.index(array[i-d])
		min_heap[-1], min_heap[to_remove] = min_heap[to_remove], min_heap[-1]
		temp = min_heap[to_remove:-1]
		hq.heapify(temp)
		min_heap.pop(0)
		min_heap[to_remove:] = temp


	if len(max_heap) != d/2 + 1:
		if array[i] <= min_heap[0]:
			hq.heappush(max_heap,array[i])
		else:
			temp = hq.heappop(min_heap)
			hq.heappush(max_heap,temp)
			hq.heappush(min_heap,array[i])
	else:
		if array[i] >= max_heap[0]:
			hq.heappush(min_heap,array[i])
		else:
			temp = hq.heappop(max_heap)
			hq.heappush(max_heap,temp)
			hq.heappush(min_heap,array[i])