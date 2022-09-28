"""
Daniel Yentin
SoftDev
K04 -- Python program to randomly select an element from a dictionary
2022-09-22
time spent: 0.5
DISCO:
    There are multiple different ways of generating randomness.
QCC:
    Why do we need to convert krewes.keys() into a list to access the keys.
OPS SUMMARY:
    1. Randomly choose a key from the list of keys in dictionary krewes.
    2. Randomly choose an devo from the value at the key.
    3. Print both.
"""

import random

PD = 0
DEVO = 1
DUCKY = 2

dict = {}
with open("krewes.txt", "r") as f:
    tempstr = f.readlines()
    templist = tempstr.split("@@@")
    for i in templist:
        templist[i] = templist[i].split("$$$")
    for i in templist:
        for _ in templist[i]:
            if templist[i][PD] not in dict:
                dict[templist[i][PD]] = [(templist[i][DEVO], templist[i][DUCKY])]
            else:
                dict[templist[i][PD]].append((templist[i][DEVO], templist[i][DUCKY]))

DEVO = 0
DUCKY = 1

rrow = random.choice(list(krewes.keys()))
rcol = random.choice(krewes[rrow])

print(f"{rrow} : {rcol[DEVO]} : {rcol[DUCKY]}")
