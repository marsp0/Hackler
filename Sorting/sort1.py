#!/bin/python
def insertionSort(ar):    
	value = ar[-1]
	#print value
	value_index = len(ar) - 1
	for index in xrange(len(ar)-2, -1,-1):
		if ar[index] > value:
			temp = ar[index]
			ar[value_index] = ar[index]
			value_index = index
			for item in ar:
				print item,
			print
		else:
			ar[value_index] = value
			break
		if value_index == 0 and ar[0] > value:
			ar[1] = temp
			ar[0] = value
	for item in ar:
		print item,
	print
	return ''

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
