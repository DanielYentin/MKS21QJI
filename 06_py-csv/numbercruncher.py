"""
Mansplaining-manipulating-malewives: Daniel Yentin, Kevin Xiao
SoftDev
K06 -- Build a dictionary from a CSV file
2022-10-03
time spent: 1
DISCO:
    rsplit() is cool
QCC:
    I dont understand how random.choices() works with inputed weights
OPS SUMMARY:
    1. Parse CSV input file
    2. Build dictionary from parsed input
    3. Pick a random weighted occupation
    4. ...?
    5. Profit
"""

from math import ceil
import random

def main() ->  None:
    krewes: dict[str, float] = build_dict("occupations.csv")
    print(krewes)

    occupation: str = pick_rand_weighted(krewes)
    print(occupation)


def build_dict(input: str) -> dict[str, float]:
    temp_dict: dict[str] = {}
    with open(input, 'r') as f:
        lines: list[str] = f.readlines()

    for i in range(1, len(lines)):
        line: str = lines[i].strip() # strip the newline of the end of each line

        """
        split() and rsplit() can be provided a second argument (after the delimitter) 
        that determines what is the maximum amount of splits that can be performed.
        
        As opposed to split, rsplit starts splitting from the right. 
        This is useful because some occupations may contain commas 
        (such as "Life, Physical and Social Science"). As such the normal split() 
        (with a max split argument) would not work as it would split on the 
        first comma in the occupation name, rather than the comma seperating the 
        occupation name and the percentage. If, however, we start from the 
        right hand side, then the first comma will always be the delimitter for the 
        key and value. Which is why we use rsplit() and not split().
        
        Thank you for coming to my ted talk.
        """
        line: list[str] = line.rsplit(',', 1) 
        
        occupation: str = line[0].strip('\"')
        percentage: float = float(line[1])
        
        temp_dict[occupation] = percentage

    return temp_dict

def pick_rand_weighted(input: dict[str, float]) -> str:
    occupations: list[str] = list(input.keys())
    percentages: list[float] = list(input.values())
    #occupation: str = random.choices(occupations, weights=percentages, k=1)[0] # weights are not correct, use diffrent method instead
    
    weighted_occupations = []
    # In the for loop below this is called unpacking in python. Simillar to how the enumerate function works 
    for k, v in input.items(): # create a list of occupations, the amount of each corresponding to their percentage (i.e. Sales : 10.2 would appear 10 times (round value up))
        for _ in range(ceil(v)): # better than using round to avoid rounding occupations with percentages < 1 to 0
            weighted_occupations.append(k)
    occupation = random.choice(weighted_occupations)
    return occupation

if __name__ == "__main__":
    main()