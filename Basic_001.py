from math import ceil, floor
from numpy.core.defchararray import isnumeric


def information():
    print("Do Arithmatic Operations between Numbers:\n")
    y = input()
    n = ["", ""]
    b = ""
    op = []
    c = ""
    l, f = 0, 0
    p = 0
    s = 0
    x = [a := i if i in range(0, y.__len__()) else i for i in y]
    for i in range(0, x.__len__()):
        while f < x.__len__():
            if x[f] == "+" or x[f] == "-" or x[f] == "*" or x[f] == "/" or x[f] == "%":
                op.append(x[f])
                f = f + 1
                while s < f-1 and op.__len__() == 1:
                    if s >= f-1:
                        break
                    n[0] = n[0] + x[s]
                    s = s + 1
                if f == x.__len__():
                    break
                if op.__len__() >= 1:
                    c = op[l]
                    p = f
                    while p < x.__len__() and l <= op.__len__() - 1:
                        print(f"Your Numbers are [1]: {n[0]}")
                        print(f"p is [in]: {p}")
                        z = f
                        if x[p] == "+" or x[p] == "-" or x[p] == "*" or x[p] == "/" or x[p] == "%":
                            while z < p:
                                b = b + x[z]
                                z = z + 1
                                print(f"z is [in]: {z}")

                            n[1] = str(n[1]) + b
                            # p = p + 1
                            while n[0] != "" and n[1] != "" and op.__len__() > 0:
                                n[0] = float(n[0])
                                n[1] = float(n[1])
                                print(f"c is [in]: {c}")
                                if c == "+":
                                    n[0] = floor(n[0] + n[1])
                                elif c == "-":
                                    n[0] = n[0] - n[1]
                                elif c == "*":
                                    n[0] = n[0] * n[1]
                                elif c == "/":
                                    n[0] = n[0] / n[1]
                                elif c == "%":
                                    n[0] = n[0] % n[1]
                                else:
                                    print(f"Invalid Operation")
                                print(f"Your Result inside loop1: {n[0]}")
                                c = op[l]
                                if l < op.__len__():
                                    l = l + 1
                                break
                        if p == x.__len__() - 1:
                            b = ""
                            n[1] = ""
                            while z <= p:
                                b = b + x[z]
                                z = z + 1
                            n[1] = str(n[1]) + b
                            print(f"Your Numbers are [2]: {n[1]}")
                            # p = p + 1
                            # break
                            while n[0] != "" and n[1] != "" and op.__len__() > 0 and p == x.__len__() - 1:
                                n[0] = float(n[0])
                                n[1] = float(n[1])
                                print(f"c is [in]: {c}")
                                if c == "+":
                                    n[0] = floor(n[0] + n[1])
                                elif c == "-":
                                    n[0] = n[0] - n[1]
                                elif c == "*":
                                    n[0] = n[0] * n[1]
                                elif c == "/":
                                    n[0] = n[0] / n[1]
                                elif c == "%":
                                    n[0] = n[0] % n[1]
                                else:
                                    print(f"Invalid Operation")
                                print(f"Your Result inside loop2: {n[0]}")
                                c = ""
                                break
                        # b = b + x[p]
                        p = p + 1
                        print(f"Your Numbers are: {c}")
                        print(f"p is [out]: {p}")

                        print(f"Your operators are: {op}")
                        print(f"Your Numbers are: {n}")
            else:
                f = f + 1


        if p == x.__len__():
            print(f"Your Result is: {n[0]}")
            break
    print(f"Final Result is: {n[0]}")


if __name__ == "__main__":
    information()
