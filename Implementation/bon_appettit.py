total_len, alergic_item = [int(v) for v in raw_input().strip().split()]
arr = [int(v) for v in raw_input().strip().split()]
charged = int(raw_input().strip())

to_pay = sum(arr)/2

if to_pay == charged:
	print arr[alergic_item]/2
else:
	print 'Bon Appetit'