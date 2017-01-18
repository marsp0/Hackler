#!/bin/python

import sys


time = raw_input().strip()

if time[-2:] == 'PM':
	if time[:2] == '12':
		print time[:-2]
	else:			
		print str(int(time[:2])+12) + time[2:-2]
else:
	if time[:2] == '12':

		print str(int(time[:2])-12).rjust(2,'0') + time[2:-2]
	else:
		print time[:-2]