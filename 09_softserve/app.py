# Yinwei Zhang
# China Rats Plus One
# SoftDev
# <K06: CSV file parsing>
# 2024-9-19
# Time Spent : 0.5 Hours

import random
import csv
from flask import Flask

app = Flask(__name__)

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

@app.route("/")

def page():
    return sel(readfile("occupations.csv"))

if __name__ == "__main__":
    app.debug = True
    app.run()