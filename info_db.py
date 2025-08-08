import sqlite3

db = sqlite3.connect("info.db")
conn = db.cursor()

course = input("Course: ")

db.commit()
query = conn.execute("SELECT * FROM info WHERE Course = ?", (course,))


for line in query:
    print(line)


db.close()