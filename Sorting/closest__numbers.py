import sys

'''https://www.hackerrank.com/challenges/closest-numbers'''

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]

def merge(array):
	if len(array) < 2:
		return array
	else:
		mid = len(array) / 2
		left = merge(array[:mid])
		right = merge(array[mid:])
		return (list(merge_arrays(left,right)))

def merge_arrays(left,right):
	new = []
	left_index = 0
	right_index = 0
	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			new.append(left[left_index])
			left_index += 1
		else:
			new.append(right[right_index])
			right_index += 1
	if left_index < len(left):
		new.extend(left[left_index:])
	if right_index < len(right):
		new.extend(right[right_index:])

	return new


array = merge(array)
result = []
current_min = sys.maxsize
for index in xrange(len(array)-1):
	if abs(array[index+1] - array[index]) < current_min:
		current_min = abs(array[index+1] - array[index])
		result = [array[index], array[index+1]]
	elif abs(array[index+1] - array[index]) == current_min:
		result.append(array[index])
		result.append(array[index+1])

print ' '.join(map(str,result))