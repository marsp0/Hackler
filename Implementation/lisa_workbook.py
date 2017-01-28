
'''https://www.hackerrank.com/challenges/lisa-workbook'''

n, k = map(int,raw_input().strip().split())
problems_chapter = map(int,raw_input().strip().split())
counter = 0
page = 1
numbers = 0
for index in xrange(1,n+1):
	temp = 1
	to_reduce = problems_chapter[index-1]
	while  to_reduce > 0:
		to_reduce -= k
		if page in [x for x in xrange((temp-1)*k+1,temp*k+1)]:
			if page <= problems_chapter[index-1]:
				counter += 1
		page += 1
		temp += 1

print counter