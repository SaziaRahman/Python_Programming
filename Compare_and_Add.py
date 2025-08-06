from numpy.core.defchararray import isnumeric

num1 = input("Enter first number: ").strip()
num2 = input("Enter second number: ").strip()

a, b = 0.0, 0.0

if isnumeric(num1) and isnumeric(num2):
    a = a + float(num1)
    b = b + float(num2)
    if num1 > num2:
        print("The first number is greater than the second number.")
    elif num1 < num2:
        print("The first number is less than the second number.")
    elif num1 == num2:
        print("The first number is equal to the second number.")
else:
    print("Invalid")

result = a + b

print(f"The Operation Result is: {result: .2f}")

