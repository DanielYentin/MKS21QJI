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


with open("krewes.txt", "r") as f:
    tempstr = f.readlines()
    templist = tempstr.split("@@@")
    for i in templist:
        templist[i] = templist[i].split("$$$")
    dict = {}
    for i in templist:
        for _ in templist[i]:
            if templist[i][PD] not in dict:
                dict[templist[i][PD]]
            else:
                dict[templist[i][PD]].append([])

krewes = {
	2: ["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
	7: ["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
	8: ["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
}

rrow = random.choice(list(krewes.keys()))
rcol = random.choice(krewes[rrow])

print(f"{rrow} : {rcol}")
