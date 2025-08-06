import sys
from mario import print_square

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    try:
        print("My name is", end=" ")
        for arg in sys.argv[1:]:
            print(arg, end=" ")
        print("-------------------")
    except IndexError:
        print("Name is not given")


if __name__ == "__main__":
    print_square(len(sys.argv))