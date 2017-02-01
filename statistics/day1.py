'''https://www.hackerrank.com/challenges/s10-basic-statistics'''

n = int(raw_input().strip())
array = [int(v) for v in raw_input().strip().split()]
#array = [int(v) for v in open('test.txt','r').read().strip().split()]
mean = '%.1f' % (sum(array)/float(n))

array = sorted(array)
if n % 2 == 1:
	med_1 = n/2
	med_2 = n/2 + 1
else:
	med_1 = n/2 - 1
	med_2 = n/2

median = (array[med_1] + array[med_2])/2.0
median = '%.1f' % median

lista = []
for item in array:
	count = array.count(item)
	lista.append([item,count])
maxa = [0,0]
for item,count in lista:
	if count > maxa[1]:
		maxa = [item,count]
modal = maxa[0]

print mean
print median
print modal