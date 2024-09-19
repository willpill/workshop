# Yinwei Zhang
# China Rats Plus One
# SoftDev
# <K06: CSV file parsing>
# 2024-9-19
# Time Spent : 0.5 Hours

import random
import csv

def readfile(f):
    dictionary = {}
    with open (f, 'r') as listfile:
        reader = csv.reader(listfile)
        next(reader)
        for row in reader:
            job = row[0]
            percent = float(row[1])
            dictionary[job] = percent
            
    print(dictionary)
        
readfile("occupations.csv")