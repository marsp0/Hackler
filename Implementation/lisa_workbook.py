n, k = map(int,raw_input().strip().split())
problems_chapter = map(int,raw_input().strip().split())
counter = 0
page = 1
numbers = 0
for index in xrange(1,n+1):
	temp = 1
	if problems_chapter[index-1] < k:
		lower_k = problems_chapter[index-1]
	else:
		lower_k = k
	to_reduce = problems_chapter[index-1]
	while  to_reduce > 0:
		to_reduce -= lower_k
		print 'chapter - ', index,' page - ', page,' lower - ', (temp-1)*lower_k,' higher - ',temp*lower_k
		if page in [x for x in xrange((temp-1)*lower_k,temp*lower_k +1)]:
			#print 'chapter - ', index,' page - ', page,' lower - ', (temp-1)*lower_k,' higher - ',temp*lower_k
			counter += 1
		page += 1
		temp += 1
		if temp*lower_k > problems_chapter[index-1]:
			lower_k = problems_chapter[index-1]%lower_k

print counter