'''https://www.hackerrank.com/challenges/marcs-cakewalk - EASY
	
	The idea here is to put the highest calories in the beginning where the multiplicative factor is low.
'''

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]

array = sorted(array, reverse=True)

result = 0
for index in xrange(len(array)):
	result += (2**(index) * array[index]) 
print result