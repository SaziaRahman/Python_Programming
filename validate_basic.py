import re

input_string = input("Please Start: ").strip()
x = [a := i if i in range(1, 11) else i for i in input_string]
n = []

if re.search(r"^[0-9]+$", input_string):
    print("Your Output:", input_string)
elif num := re.search(r"^([0-9]+)(\^|\*|/|-|\+|%)([0-9]+)$", input_string):
    if num.group(2) == "^":
        n.append(int(num.group(1)) ** int(num.group(3)))
    elif num.group(2) == "*":
        n.append(int(num.group(1)) * int(num.group(3)))
    elif num.group(2) == "/":
        n.append(int(num.group(1)) / int(num.group(3)))
    elif num.group(2) == "-":
        n.append(int(num.group(1)) - int(num.group(3)))
    elif num.group(2) == "+":
        n.append(int(num.group(1)) + int(num.group(3)))
    elif num.group(2) == "%":
        n.append(int(num.group(1)) % int(num.group(3)))
else:
    print("Invalid Input")

print("Your Result:", n)