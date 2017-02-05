'''https://www.hackerrank.com/challenges/insertion-sort'''

tests = []
result = []

def mergesort(ar):
    shifts = 0
    if len(ar)>1:
        mid=len(ar)/2
        left,right=ar[:mid],ar[mid:]
        shifts +=mergesort(left)
        shifts +=mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                ar[k]=left[i]
                i+=1
            else:
                ar[k]=right[j]
                j+=1
                shifts+=mid-i
            k+=1
        while i<len(left):
            ar[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            ar[k]=right[j]
            j+=1
            k+=1
    return shifts
n = input()
for iterate in range( n ):
    x = input()
    a = [ int( i ) for i in raw_input().strip().split() ]
    tests.append(a)

for test in tests:
	result.append(mergesort(test))

for item in result:
	print item