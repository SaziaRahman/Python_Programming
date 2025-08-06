import csv

with open("info.csv", "r") as file:
    lines = csv.DictReader(file)
    totalStudents = {}
    for row in lines:
        name = row["Name"] 
        course = row["Course"]
        roll = row["Roll"]
        print(f"Student, {name} having roll no. {roll}, has taken {course}")
        if course in totalStudents:
            totalStudents[course][course] += {name}
        else:
            totalStudents[course] = {course: [name]}


for course in totalStudents:
    print(f"{course}: {totalStudents[course]}")

