# your heading here

from cProfile import run
from flask import Flask

import csv
import random

def createDict():
    jobs = {}
    with open('occupations.csv') as f:
        r = csv.reader(f)
        next(r)
        for line in r:
            jobs[line[0]] = float(line[1])
        return jobs

def chooseJob(jobs):
    return random.choices(list(jobs.keys()), weights=jobs.values())
    # target_sum = random.randint(0, int(jobs["Total"]))
    # running_sum = 0
    # for k, v in jobs[:-1]:
    #     if running_sum+v > target_sum:
    #         return k
    #     running_sum += v


app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    jobs = createDict()
    return chooseJob(jobs)

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
	This is not a secure connection so "http" must be used instead of "https"

QCC:
0. Java
1. The root directory
2. The terminal.
3. The name of this file
4. The website. I tested it
5. Processing
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
