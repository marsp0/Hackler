'''https://www.hackerrank.com/challenges/cut-the-sticks'''

def quick_sort(array):
	if len(array) <= 1:
		return array
	else:
		low = []
		high = []
		pivot = []
		piv_el = array[0]

		for element in array:
			if element > piv_el:
				high.append(element)
			elif element < piv_el:
				low.append(element)
			else:
				pivot.append(element)

		high = quick_sort(high)
		low = quick_sort(low)

		return high + pivot + low


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr = quick_sort(arr)
print len(arr)
while True:
	if len(arr) > 1:
		min_element = arr.pop()
		for index in xrange(len(arr)-1, -1, -1):
			if arr[index] - min_element <= 0:
				arr.pop(index)
			elif arr[index] - min_element > 0:
				break
		if len(arr) > 0:
			print len(arr)
	else:
		break