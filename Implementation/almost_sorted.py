from collections import defaultdict

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
arrays = defaultdict(set)
temp = 0
index = 0
while index < n:
	while True:
		try:
			if array[index] > array[index+1]:
				arrays[temp].add(index)
				arrays[temp].add(index+1)
				index += 1
			else:
				break
		except IndexError:
			break
	index  += 1

if len(arrays.keys()) > 1:
	print 'no'
print arrays