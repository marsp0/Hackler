skills = raw_input().strip()
dicta = {key:0 for key in ['p','c','m','z','b']}
for i in skills:
	dicta[i] += 1

if 0 in dicta.values():
	print 0
else:
	print min(dicta.values())