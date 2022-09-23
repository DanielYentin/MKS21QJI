"""
Jasmine Yuen
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

krewes = {
    2 : ["devo1", "devo2", "devo3"],
    7 : ["devo1", "devo2", "devo3"],
    8 : ["devo1", "devo2", "devo3"]
}

rrow = random.choice(list(krewes.keys()))
rcol = random.choice(krewes[rrow])

print(f"{rrow} : {rcol}")
