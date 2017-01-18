#!/bin/python

import sys
import math


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

looper = min(b)
results = []
to_pop = set()
for index in xrange(1,looper+1):
    
    a_counter = 0
    for integer in a:
        if index%integer != 0:
            break
        a_counter += 1
    if a_counter == len(a):
        results.append(index)
for index in xrange(len(results)):
    for integer in b:
        if integer % results[index] != 0:
            to_pop.add(results[index])
            
for item in to_pop:
    results.pop(results.index(item))
print len(results)