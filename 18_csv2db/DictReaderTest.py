# Ivan Yeung Daniel Yentin
# SoftDev
# K18 -- (Python+SQLite)3: A Mare Widge Made in Hebben
# 2022-10-25
# time spent: .3

import csv       #facilitate CSV I/O

with open("students.csv") as csv_file: #opening the csv file with csv_file as the variable name
#with key word automatically deals with closing the csv once you leave the with block
    reader = csv.DictReader(csv_file) # csv.DictReader creates dicts for each line with field names as keys and things that fall under it as values
    #Ex: alison,23,10 ---> {name: alison, age: 23, id: 10}
    #NOTE the keys of the dictionary is based on the header and the value paired to it is in its column
    print("DictReader rows: ")
    for row in reader:
    #After looping over the csv once, looping over it again will return nothing since you already reached the end.
    #In order to loop over the file again, you need to reopen the csv.
        print(row) # print to view each dictionary

#Opening file again to print individual keys
with open("students.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    counter = 0
    for row in reader:
        #can print specific items of the csv by specifying the key
        name = row['name']
        age = row['age']
        id = row['id']
        print("-" * 30 +f"STUDENT {counter}"+ "-" * 30)
        print(f"Student's name: {name}")
        print(f"Student's age: {age}")
        print(f"Student's id: {id}")
        counter += 1
