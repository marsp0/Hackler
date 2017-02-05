
n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
in_array = list(array)
q_counter = 0

def insertion_sort(array):
	counter = 0
	for i in xrange(len(array)):
		j = i
		while (j > 0) and (array[j] < array[j-1]):
			counter += 1
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
	return array, counter

ar,in_counter = insertion_sort(in_array)



def partition(array,low,high):
	global q_counter
	pivot = array[high]
	i = low
	for j in xrange(low,high):
		if array[j] <= pivot:
			array[i], array[j] = array[j], array[i]
			q_counter += 1
			i += 1
	q_counter += 1
	array[i], array[high] = array[high], array[i]
	return i

def quicksort(array,low,high):
	if len(array) < 2:
		return array
	else:
		if low < high:
			p = partition(array, low, high)
			quicksort(array,low,p-1)
			quicksort(array,p+1,high)

quicksort(array, 0, len(array)-1)

print in_counter - q_counter