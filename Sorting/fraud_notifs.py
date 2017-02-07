import bisect
from math import ceil

'''https://www.hackerrank.com/challenges/fraudulent-activity-notifications'''

n , d = [int(v) for v in raw_input().strip().split()]
#array = [int(v) for v in raw_input().strip().split()]
array = [int(v) for v in open('test.txt','r').read().split()]
d_array = []
notifs = 0

for index in xrange(d):
	bisect.insort(d_array,array[index])

for index in xrange(d,n):

	if d % 2 == 0:

		first = d_array[len(d_array)/2]
		second = d_array[len(d_array)/2 - 1]
		median = (first+second)/2.0

	else:
		median = d_array[len(d_array)/2]
		#print len(d_array)/2 , median

	if array[index] >= 2*median:
		notifs += 1

	to_remove = bisect.bisect(d_array, array[index - d]) - 1
	#print 2*median , array[index] , d_array
	d_array.pop(to_remove)
	bisect.insort(d_array, array[index])

print notifs