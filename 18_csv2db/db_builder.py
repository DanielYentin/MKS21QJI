#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

with open("students.csv", 'r') as students:
    students = csv.DictReader(students)

# command = ""          # test SQL stmt in sqlite3 shell, save as string
# c.execute(command)    # run SQL statement

    c.execute("create table students(name text, age int, id int)")
    for row in students:
        name = row['name']
        age = row['age']
        id = row['id']
        
        c.execute(f"insert into students values('{name}', {age}, {id})")
#==========================================================

db.commit() #save changes
db.close()  #close database


