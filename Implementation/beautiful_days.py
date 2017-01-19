start,end,k = [int(v) for v in raw_input().strip().split()]
counter = 0

def reverse(number):
	number = str(number)
	to_return = ''
	for index in xrange(len(number)-1,-1,-1):
		to_return += number[index]
	return int(to_return)

for x in xrange(start,end+1):
	if abs(x-reverse(x)) % k == 0:
		counter += 1

print counter
