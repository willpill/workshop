# Yinwei Zhang, Aditya Anand, Caden Khuu
# Smelly Lobotomy
# SoftDev
# K13 <Occupations table format>
# 2024-9-30
# Time Spent : 1 Hour

import random
import csv
from flask import Flask, render_template

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
            link = row[2]
            d[job] = {"percent": percent, "link": link}
    return d
        
        
def sel(d):
    jobs = []
    percentages = []
    for job in d:
        jobs.append(job)
        percentages.append(d[job]["percent"])
    return random.choices(jobs, weights=percentages, k=1)[0]

@app.route("/")

def page():
    allocc = readfile("data/occupations.csv")
    occ = sel(allocc)
    print (occ)
    return render_template("tablified.html", occupations=allocc, selected=occ)

if __name__ == "__main__":
    app.debug = True
    app.run()
