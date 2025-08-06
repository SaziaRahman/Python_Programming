import csv

with open("info.csv", "r") as file:
    lines = csv.DictReader(file)
    for row in lines:
        name = row["Name"] 
        course = row["Course"]
        roll = row["Roll"]
        print(f"Student, {name} having roll no. {roll}, has taken {course}")