'''https://www.hackerrank.com/challenges/jim-and-the-orders?h_r=next-challenge&h_v=zen - EASY'''

n = int(raw_input().strip())
hash_table = {}
for i in xrange(1,n+1):
	order_time,process_time = [int(v) for v in raw_input().strip().split()]
	hash_table[i] = (order_time,process_time,i)

array = sorted(hash_table.values(), key = lambda item: (item[0]+item[1], item[2]))
for item in array:
	print item[2],