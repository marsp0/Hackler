from collections import defaultdict

n = int(raw_input().strip())
database = defaultdict(list)
for i in xrange(n):
	number, string = raw_input().strip().split()
	if i >= n/2:
		database[int(number)].append(string)
	else:
		database[int(number)].append('-')
#at thius point we can just print the elements of the defaultdict and they will be sorted
#we wont do it because that was not the exercise :D

index = 0
while index < n:
	for item in database[index]:
		print item,
	index += 1