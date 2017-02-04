def insertion_sort(array):
	counter = 0
	for i in xrange(len(array)):
		j = i
		while (j > 0) and (array[j] < array[j-1]):
			counter += 1
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
	return array, counter

m = input()
ar = [int(i) for i in raw_input().strip().split()]
ar,counter = insertion_sort(ar)
#print " ".join(map(str,ar))
print counter