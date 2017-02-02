string = raw_input().strip()
result = ''
index = 0
while index < len(string):
	try:
		if string[index] == string[index+1]:
			index += 2
			continue
		else:
			result += string[index]
			index += 1
	except IndexError:
		result += string[index]
		index += 1
if result == '':
	print 'Empty String'
else:
	print result

