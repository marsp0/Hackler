n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
array_2 = list(reversed(array))

def some_func(n,array):
	sorted_array = sorted(array)
	database = {array[index] : index for index in xrange(n)}

	swaps = 0

	for index in xrange(n):

		if array[index] != sorted_array[index]:
			swaps += 1
			to_swap = database[sorted_array[index]]
			database[array[index]] = to_swap
			array[index], array[to_swap] = array[to_swap], array[index]

	return swaps

swap_1 =  some_func(n,array)
swap_2 = some_func(n,array_2)
print min(swap_1,swap_2)