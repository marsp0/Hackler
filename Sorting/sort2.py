#!/bin/python
def insertionSort(ar):    
	i = 1
	while i < len(ar):
		j = i
		while j > 0 and ar[j] < ar[j-1]:
			ar[j], ar[j-1] = ar[j-1], ar[j]
			j -= 1
		i+= 1
		for item in ar:
			print item,
		print

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
