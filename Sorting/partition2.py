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
		print ' '.join(map(str,left + [pivot] + right)).strip()
		return left + equal + right

m = input()
ar = [int(i) for i in raw_input().strip().split()]
array = partition(ar)
pivot = ar[0]
#print ' '.join(map(str,array))