"""
Daniel Yentin
SoftDev
K05 -- Python program to randomly select an element from a dictionary that is read from an input file
2022-09-29
time spent: 0.5
DISCO:
	There are multiple different ways of parsing input
QCC:
	
OPS SUMMARY:
	1. 
"""

import random

krewes = {}
with open("krewes.txt", "r") as f:
	tempstr = f.read().strip() # read in the file and remove trailing \n character
	templist = tempstr.split("@@@") # split string along the "@@@" delimitter into a list 
	for i in range(len((templist))): 
		templist[i] = templist[i].split("$$$") # split each item along the "$$$" delimitter into a list containing the Period, Devo, and Ducky
	for i in range(len((templist))):

		period = int(templist[i][0]) # to make keys be integers and not strings
		devo = templist[i][1]
		ducky = templist[i][2]

		# add the devo ducky pair into the correct pair
		if period not in krewes:
			krewes[period] = [(devo, ducky)]
		else:
			krewes[period].append((devo, ducky))

period = random.choice(list(krewes.keys()))
DevoDucky = random.choice(krewes[period])
devo = DevoDucky[0]
ducky = DevoDucky[1]

print(f"{period} : {devo} : {ducky}")
