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
# command = ""          # test SQL stmt in sqlite3 shell, save as string
# c.execute(command)    # run SQL statement

with open("students.csv", 'r') as students:
    db.execute("DROP TABLE if exists students")
    students = csv.DictReader(students)
    c.execute("create table students(name text, age int, id int)")

    for row in students:
        name = row['name']
        age = row['age']
        id = row['id']
    
        c.execute(f"insert into students values('{name}', {age}, {id})")

with open("courses.csv", 'r') as courses:
    db.execute("DROP TABLE if exists courses")
    courses = csv.DictReader(courses)
    c.execute("create table courses(code text, mark int, id int)")

    for row in courses:
        code = row['code']
        mark = row['mark']
        id = row['id']
        
        c.execute(f"insert into courses values('{code}', {mark}, {id})")
#==========================================================

db.commit() #save changes
db.close()  #close database


