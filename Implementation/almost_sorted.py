from collections import defaultdict

n = int(raw_input().strip())
#array = [int(v) for v in raw_input().strip().split()]
array = [int(v) for v in open('test.txt','r').read().strip().split()]
index = 0
p1 = -1
p2 = -1

while index < n:
	while index < n:
		try:
			if array[index] > array[index+1] and p1 == -1:
				p1 = index
				index += 1
			elif array[index] > array[index+1] and p1 != -1:
				index += 1
			else:
				if array[index] < array[index+1] and (p1 != -1 and array[index] < array[index-1]):
					p2 = index
					index += 1
				else:
					index += 1
					break
		except IndexError:
			if p1 != -1 and p2 == -1:
				p2 = index
			index += 1
			break

if p1 == -1 and p2 == -1:
	if sorted(array) == array:
		print 'yes'

elif p2 - p1 == 1:
	array[p2], array[p1] = array[p1], array[p2]
	if sorted(array) == array:
		print 'yes'
		print 'swap {} {}'.format(p1+1, p2+1)
	else:
		print ';ds'
		print 'no'
elif p2 - p1 > 1:
	temp = array[p1:p2+1]
	temp = sorted(temp)
	temp_array = array[:p1] + temp + array[p2+1:]
	if temp_array == sorted(array):
		print 'yes'
		print 'reverse {} {}'.format(p1+1,p2+1)
	else:
		print 'no'