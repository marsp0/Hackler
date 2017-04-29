'''https://www.hackerrank.com/challenges/maxsubarray'''

tests = int(raw_input().strip())

def max_subarray_contiguous(A):
	max_ending_here = max_so_far = A[0]
	for x in A[1:]:
		max_ending_here = max(x, max_ending_here + x)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

def max_subarray(array):
	sum_elements = 0
	for element in array:
		if element > 0:
			sum_elements+= element
	if sum_elements == 0:
		sum_elements = max(array)
	return sum_elements

for i in xrange(tests):
	n = int(raw_input().strip())
	array = [int(v) for v in raw_input().strip().split()]
	print max_subarray_contiguous(array), max_subarray(array)