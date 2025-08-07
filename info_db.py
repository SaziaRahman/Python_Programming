import sqlite3

db = sqlite3.connect("info.db")

course = input("Course: ")

db.commit()
query = db.execute("SELECT Name FROM info WHERE Course= '"+ course +"'")


for line in query:
    print(line)


db.close()