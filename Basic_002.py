def input_information():
    '''parameters:
    (1)Positional Parameters(example: When we pass values to the print statement),
    (2)Named Parameters(example: When we pass value to the optional arguments, such as: "sep", "end"),
    '''
    print('Hello "Friend"')
    print("\"Please\"", end=" ")
    print("Answer the questions.")
    Name = input("What is your name?\n").strip().title()
    # strip() removes the white space and title() capitalizes each word of the string.
    print("hello, ", Name, "!", sep="")
    Color = input("What is your favorite color?\n")
    Color = Color.capitalize()
    # capitalized() capitalizes first word of the string.
    print("My favorite color is " + Color)
    Age = input("What is your age?\n")
    print(f"My age is {Age}")
    first, last = Name.split(" ")

    def print_information():
        print(f'''
        {first}\'s Information:
        Name: {Name}
        Favorite Color: {Color}
        Age: {Age}
        ''')
    print_information()


if __name__ == "__main__":
    input_information()



