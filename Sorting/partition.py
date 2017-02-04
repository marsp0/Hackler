#!/bin/python
def partition(ar):
	if len(ar) <= 1:
		return ar
	else:
		left, equal, right = [], [], []
		pivot = ar[0]
		for element in ar:
			if element > pivot:
				right.append(element)
			elif element < pivot:
				left.append(element)
			else:
				equal.append(element)
		left = partition(left)
		right = partition(right)
		return left + equal + right , pivot

m = input()
ar = [int(i) for i in raw_input().strip().split()]
array,pivot = partition(ar)
print ' '.join(map(str,array[:array.index(pivot)]))
print ' '.join(map(str,array[array.index(pivot)+1:]))
print array