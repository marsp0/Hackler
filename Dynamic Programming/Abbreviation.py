import sys

sys.setrecursionlimit(100000)

#n = int(raw_input().strip())
fish = open('test.txt','r')
n = int(fish.readline().strip())

def check(end1,end2,string1,string2, memo):
	if (end1,end2) in memo:
		return memo[(end1,end2)]
	else:
		if string1[:end1+1] == '' or string2[:end2+1] == '':
			memo[(end1,end2)] = 0
		elif string1[end1].lower() == string2[end2].lower():
			if string1[end1] == string1[end1].lower():
				first = 1+check(end1-1,end2-1,string1,string2,memo)
				second = check(end1-1,end2,string1,string2,memo)
				if second >= first:
					memo[(end1,end2)] = second
				else:
					memo[(end1,end2)] = first					
			else:
				memo[(end1,end2)] = 1 + check( end1-1, end2-1,string1,string2,memo)
		else:
			memo[(end1,end2)] = check(end1-1,end2,string1,string2,memo)
	return memo[(end1,end2)]

for i in xrange(0,n):
	#string1 = raw_input().strip()
	#string2 = raw_input().strip()
	string1 = fish.readline().strip()
	string2 = fish.readline().strip()
	initial_memo = {}
	upper_letters = []
	for i in xrange(len(string1)):
		if string1[i] == string1[i].upper():
			upper_letters.append(string1[i])
	check(len(string2)-1,len(upper_letters)-1,string2,''.join(upper_letters),initial_memo)
	if initial_memo[(len(string2)-1,len(upper_letters)-1)] != len(upper_letters):
		print 'NO'
	else:
		memo = {}
		check(len(string1)-1,len(string2)-1,string1,string2,memo)
		if memo[(len(string1)-1,len(string2)-1)] != len(string2):
			print 'NO'
		else:
			print memo[(len(string1)-1,len(string2)-1)]
			print 'YES'