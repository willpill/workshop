# Yinwei Zhang
# China Rats Plus One
# SoftDev
# <K06: CSV file parsing>
# 2024-9-19
# Time Spent : 0.5 Hours

import random
import csv

def readfile(f):
    d = {}
    with open (f, 'r') as listfile:
        reader = csv.reader(listfile)
        next(reader)
        for row in reader:
            job = row[0]
            if job == "Total":
                continue
            percent = float(row[1])
            d[job] = percent
    return d
        
        
def sel(d):
    return random.choices(list(d.keys()), weights=d.values(), k=1)[0]
#Find all dict keys and then convert that into a list.
#Then set the weights of random selection with the list of percentages
#Select one thing, only the first element to remove the ['']
    
print(sel(readfile("occupations.csv")))