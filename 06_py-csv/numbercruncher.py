"""
Mansplaining-manipulating-malewives: Daniel Yentin, Kevin Xiao
SoftDev
K06 -- 
2022-10-03
time spent: 0.5
DISCO:

QCC:

OPS SUMMARY:

"""

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

    for i in range(1, len(lines)-1):
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
    occupation: str = random.choices(occupations, weights=percentages, k=1)[0] # weights are not correct
    return occupation

if __name__ == "__main__":
    main()