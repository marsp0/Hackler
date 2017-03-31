grades = int(raw_input().strip())
for i in xrange(grades):
	grade = int(raw_input().strip())
	multiplier = grade / 10
	mod = grade % 10
	if grade < 38:
		print grade
		continue
	if mod < 5:
		if 5 - mod < 3:
			grade = multiplier * 10 + 5
	else:
		if (multiplier+1) * 10 - grade  < 3:
			grade = (multiplier+1) * 10
	print grade