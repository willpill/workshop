# Yinwei Zhang
# China Rats Plus One
# SoftDev
# <K05: Read file, parse list and random selection>
# 2024-9-18
# Time Spent : 0.5 Hours

import random

def read(f):
    file = open(f, 'r')
    ls = file.read().split('@@@')  # Split to list of strings separated by @@@
    entries = []
    for entry in ls:
        item = entry.split('$$$')  # Split this entry in the list of strings into another list of strings
        entries.append(
            {'period': item[0], 'devo': item[1], 'ducky': item[2]})  # add to dictionary with the info from current item
    return entries

def printtfinal(entry):
    print(f"Period: {entry['period']}, Name: {entry['devo']}, Ducky: {entry['ducky']}")  # use f string interpolation

printtfinal(random.choice(read('krewes.txt')))
