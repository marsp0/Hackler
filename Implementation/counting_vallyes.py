n = int(raw_input().strip())
steps = raw_input().strip()
counter = 0
valleys = 0
start = 0
is_valley = False
for item in steps:
	if item == 'D':
		if counter == 0:
			is_valley = True
		counter -= 1
	elif item == 'U':
		counter += 1
	if start != 0 and counter == 0:
		if is_valley:
			valleys += 1
			counter = 0
			is_valley = False
	start += 1

print valleys
