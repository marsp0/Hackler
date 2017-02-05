'''https://www.hackerrank.com/challenges/find-the-median'''


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

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]

array = merge(array)
print array[n/2]