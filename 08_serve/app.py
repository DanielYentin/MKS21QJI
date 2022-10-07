# your heading here

from cProfile import run
from flask import Flask

import csv
import random

def createDict(filename: str) -> dict[str, float]:
    '''
    Returns a dictionary from a csv 
    '''
    jobs = {}
    with open(filename) as f:
        r = csv.reader(f)
        next(r)
        for line in r:
            jobs[line[0]] = float(line[1])
        jobs.pop("Total")        
        return jobs

def chooseRandomWeightedJob(jobs: dict[str, float]) -> str:
    '''
    Returns a random weighted key from the dictionary
    '''
    return random.choices(list(jobs.keys()), weights=jobs.values())[0]
    # target_sum = random.randint(0, int(jobs["Total"]))
    # running_sum = 0
    # for k, v in jobs[:-1]:
    #     if running_sum+v > target_sum:
    #         return k
    #     running_sum += v

def keysAsString(jobs: dict[str, float]) -> str:
    '''
    Return keys of a dictionary as a string
    '''
    keys = list(jobs.keys())
    keyString = "<br>".join(keys)
    return keyString


app = Flask(__name__)

@app.route("/")
def main() -> None:
    '''
    Return a string contating:
        TNPG & roster,
        list of occupations,
        random weigted occupation
    '''
    print(__name__)

    returnList = []
    
    returnList.append("JAD: Abid Talukder, Jonathan Song, Daniel Yentin")
    returnList.append("<br>")
    print("added TNPG and Roster")
    
    returnList.append(keysAsString(jobs))
    returnList.append("<br>")
    print("added list of jobs")

    returnList.append("Random selected job: " + chooseRandomWeightedJob(jobs))
    print("added random jobs")

    return "<br>".join(returnList)

jobs = createDict("occupations.csv")
app.run()


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
