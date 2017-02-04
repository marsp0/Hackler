n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]

def partition(array,low,high):
	#print 'Low - {} , high - {}'.format(low,high)
	#print 'Current pivot is {}'.format(array[high])
	pivot = array[high]
	#print 'i - {}'.format(low)
	i = low
	#print 'looping from {} to {}'.format(low,high)
	for j in xrange(low,high):
		#print 'Checking to see if {} < {}'.format(array[j],pivot)
		#print 'their indeces are {} and {}'.format(j, high)
		if array[j] <= pivot:
			#print 'it is true'
			#print 'swapping {} and {}'.format(array[i],array[j])
			#print 'their indeces are {} and {}'.format(i,j)
			array[i], array[j] = array[j], array[i]
			i += 1
			#print 'current i is - {}'.format(i)
	#print 'swapping {} and {}'.format(array[i],array[high])
	#print 'their indeces are {} and {}'.format(i,high)
	array[i], array[high] = array[high], array[i]
	#print 
	return i

def quicksort(array,low,high):
	if len(array) < 2:
		return array
	else:
		if low < high:
			#print 'partitioning from {} to {}'.format(low,high)
			p = partition(array, low, high)
			print ' '.join(map(str,array))
			#print 'pivot index is {}'.format(p)
			#print 'pivot element is {}'.format(array[p])
			#print 'starting quicksort from {} to {}'.format(low,p-1)
			quicksort(array,low,p-1)
			#print 'finished quicksorting from {} to {}'.format(low,p-1)
			#print 'start quicksorting from {} to {}'.format(p+1,high)
			quicksort(array,p+1,high)
			#print 'finished quicksorting from {} to {}'.format(p+1,high)

quicksort(array, 0, len(array)-1)
