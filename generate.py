import random

color = random.choice(['red', 'green', 'blue', 'yellow', 'orange', 'purple'])
cards = ["KING", "QUEEN", "JACK"]
random.shuffle(cards)
print("After Shuffling Cards:", [y for y in cards])
print("----", color, " color----", sep="")

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Number between a & b:", random.randint(a, b))