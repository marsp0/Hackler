'''https://www.hackerrank.com/challenges/reduced-string - easy'''

array = list(raw_input().strip())

index = 0
counter = 1
while array:
	if index+1 >= len(array):
		if counter >= 2:
			break
		else:
			index = 0
			counter += 1
	else:
		if array[index] == array[index+1]:
			array.pop(index)
			array.pop(index)
			counter = 0
		else:
			index += 1


if array == []:
	print 'Empty String'
else:
	print ''.join(array)