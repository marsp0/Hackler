from math import ceil

to_find = int(raw_input().strip())
n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]

def binary_search(array,element):
	low = 0
	mid = len(array)/2
	high = len(array)-1

	while low < high:

		if element == array[mid]:
			return mid
		elif element > array[mid]:
			low = mid
		else:
			high = mid
		mid = int(ceil((high + low)/2.0))

print binary_search(array,to_find)