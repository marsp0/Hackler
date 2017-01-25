
'''https://www.hackerrank.com/challenges/kaprekar-numbers'''

def is_kaprekar(number):
	squared_number = str(number**2)
	if int(squared_number) < 10:
		if number == int(squared_number):
			return True
		else:
			return False
	else:
		divider = len(str(number))
		if squared_number[divider:] == '' or int(squared_number[-divider:]) == 0:
			return squared_number == number
		else:
			if number == (int(squared_number[:-divider]) + int(squared_number[-divider:])):
				return True
			return False

lower = int(raw_input().strip())
higher = int(raw_input().strip())
results = []
for i in xrange(lower,higher+1):
	if is_kaprekar(i):
		results.append(i)
if results == []:
	print 'INVALID RANGE'
else:
	for item in results:
		print item,