n, k = map(int,raw_input().strip().split(" "))
arr = map(int,raw_input().strip().split(" "))

d = {x:[] for x in range(k)}
for i in range(n): 
	d[arr[i]%k].append(arr[i])
count = 0
if len(d[0]) > 0:
	count = 1
S = set([(x,k-x) for x in range(1,k//2+1)])
for i,j in S:
	if i != j:
		if len(d[i]) > len(d[j]):
			count += len(d[i])
		else:
			count += len(d[j])
	else:
		if len(d[i]) > 0:
			count += 1
print count