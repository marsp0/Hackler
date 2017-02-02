n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
array = sorted(array)
print array

def get_meds(array):
	n = len(array)
	if n % 2 == 0:
		med_1 = n/2 - 1
		med_2 = n/2
	else:
		med_1 = n/2
		med_2 = 0
	return (med_1,med_2)

med_1,med_2 = get_meds(array)
if med_2 == 0:	
	Q_2 = array[med_1]
else:
	Q_2 = (array[med_1] + array[med_2])/2

if n % 2 == 1:
	lower_stop = n / 2
	upper_stop = n/2 + 1
else:
	lower_stop = n/2 - 1
	upper_stop = n/2 + 1

lower = array[:lower_stop]
med_1,med_2 = get_meds(lower)
print med_1,med_2, lower
if med_2 == 0:
	Q_1 = lower[med_1]
else:
	Q_1 = (lower[med_1] + lower[med_2])/2

upper = array[upper_stop:]
med_1, med_2 = get_meds(upper)
print med_1,med_2, upper
if med_2 == 0:
	Q_3 = upper[med_1]
else:
	Q_3 = (upper[med_1] + upper[med_2])/2

print Q_1
print Q_2
print Q_3