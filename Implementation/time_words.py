#!/bin/python

'''https://www.hackerrank.com/challenges/the-time-in-words'''

import sys


h = raw_input().strip()
m = raw_input().strip()
min_var_pl = ' minutes'
min_var_sl = ' minute'

minutes = {
	'01' : 'one minute',
	'02' : 'two minutes',
	'03' : 'three minutes',
	'04' : 'four minutes',
	'05' : 'five minutes',
	'06' : 'six minutes', 
	'07' : 'seven minutes',
	'08' : 'eight minutes',
	'09' : 'nine minutes',
	'10' : 'ten minutes',
	'11' : 'eleven minutes',
	'12' : 'twelve minutes',
	'13' : 'thirteen minutes',
	'14' : 'fourteen minutes',
	'16' : 'sixtheen minutes',
	'17' : 'seventeen minutes',
	'18' : 'eighteen minutes',
	'19' : 'nineteen minutes',
	'20' : 'twenty minutes',
	'21' : 'twenty one minutes',
	'22' : 'twenty two minutes',
	'23' : 'twenty three minutes',
	'24' : 'twenty four minutes',
	'25' : 'twenty five minutes',
	'26' : 'twenty six minutes',
	'27' : 'twenty seven minutes',
	'28' : 'twenty eight minutes',
	'29' : 'twenty nine minutes',

}

hours = {
	'1' : 'one',
	'2' : 'two',
	'3' : 'three',
	'4' : 'four',
	'5' : 'five',
	'6' : 'six',
	'7' : 'seven',
	'8' : 'eight',
	'9' : 'nine',
	'10' : 'ten',
	'11' : 'eleven',
	'12' : 'twelve'
}

construct_minutes = ''
hour = hours[h]
try:
	construct_minutes = minutes[m] + ' past '
	result = construct_minutes + hour
except KeyError:
	if m == '00':
		construct_minutes = " o' clock"
		result = hour + construct_minutes
	elif m == '15':
		result = 'quarter past ' + hour
	elif m == '45':
		result = 'quarter to ' + hours[str(int(h)+1)]
	elif m =='30':
		result = 'half past ' + hour
	else:
		temp = 60 - int(m)
		if temp < 10:
			temp = minutes['0' + str(temp)]
		else:
			temp = minutes[str(temp)]
		result = temp + ' to ' + hours[str(int(h)+1)]
print result