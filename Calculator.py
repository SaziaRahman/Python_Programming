from numpy.core.defchararray import isnumeric


def print_output():
    try:
        print("Calculator Input:", end="")
        Calculator_input = output()
        operation(Calculator_input)
    except TypeError:
        pass


def output():
    while True:
        try:
            in1 = input("\n(Enter 'c' to exit)\n-----Start-----:")
            if in1 == "":
                continue
            elif in1 == "c":
                return operation(in1)
            else:
                return operation(in1)
        except NameError:
            pass


def operators(a, b, d):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        pass
    try:
        if d == "^":
            a = a ** b
        elif d == "*":
            a = a * b
        elif d == "/":
            try:
                a = a / b
            except ZeroDivisionError:
                a = ""
                pass
        elif d == "-":
            a = a - b
        elif d == "+":
            a = a + b
        elif d == "%":
            a = a % b
        else:
            print(f"Operation Failed")
    except TypeError:
        pass
    return a, d


def operation(in1):
    global d
    y = in1
    n = ["", ""]
    b = ""
    op = []
    c = ""
    l, f = 0, 0
    p = 0
    s = 0
    m = []
    x = [a := i if i in range(1, 11) else i for i in y]

    for i in x:
        if i == "(":
            x.remove("(")
        if i == ")":
            x.remove(")")

    in1 = ""
    for i in x:
        in1 = in1 + i

    for i in range(0, x.__len__()):
        while f < x.__len__():
            if x[f] == "+" or x[f] == "-" or x[f] == "*" or x[f] == "/" or x[f] == "%" or x[f] == "^":
                op.append(x[f])
                f = f + 1
                while s < f - 1 and op.__len__() == 1:
                    if s >= f - 1:
                        break
                    b = b + x[s]
                    s = s + 1
                m.append(b)
                m.append(op[l])
                if f == x.__len__():
                    break
                if op.__len__() >= 1:
                    c = op[l]
                    p = f
                    while p < x.__len__() and l <= op.__len__() - 1:
                        z = f
                        if x[p] == "+" or x[p] == "-" or x[p] == "*" or x[p] == "/" or x[p] == "%" or x[p] == "^":
                            while l < op.__len__():
                                l = l + 1
                                b = ""
                                n[1] = ""
                                while z < p:
                                    b = b + x[z]
                                    z = z + 1

                                # -----------------------------------------------------
                                '''while n[0] != "" and n[1] != "" and op.__len__() > 0:
                                    n[0], n[1], c = operators(n[0], n[1], c)
                                    l = l + 1
                                    break'''
                                if l < op.__len__() - 1:
                                    l = l + 1
                                else:
                                    break
                        elif p == x.__len__() - 1:
                            b = ""
                            n[1] = ""
                            while z <= p:
                                b = b + x[z]
                                z = z + 1
                            m.append(b)
                            while op.__len__() > 0:
                                l = l + 1
                                break
                            # -----------------------------------------------------
                            '''while n[0] != "" and n[1] != "" and op.__len__() > 0:
                                n[0], n[1], c = operators(n[0], n[1], c)
                                l = l + 1
                                break'''
                        p = p + 1
            else:
                f = f + 1
        symbol = {"^": 1, "*": 2, "/": 3, "-": 4, "+": 5, "%": 6}
        k = len(op)-1
        ol = op
        j = len(op)-1
        if op.__len__() > 1:
            d = []
            for z in range(0, op.__len__()-1):
                if op[z] == op[z + 1]:
                    r = symbol[op[z]]
                    q = symbol[op[z + 1]]
                else:
                    r = min(symbol[op[z]], symbol[op[z + 1]])
                    q = max(symbol[op[z]], symbol[op[z + 1]])
                symbol_copy = [r, q]
                d0 = [key1 for key1, value in symbol.items() if value == symbol_copy[0]]
                d1 = [key1 for key1, value in symbol.items() if value == symbol_copy[1]]
                d.append(d0[0])
                d.append(d1[0])
        else:
            if op.__len__() == 0:
                break
            d = []
            d.append(str(op[0]))
        while k >= 0:
            while j >= 0:
                while op.__len__() > 0:
                    if m[0] == "":
                        m[0] = "0"
                    print(f"------?------: {m[j]}{op}{m[j-1]}")
                    print(k)
                    if m[j] == d[k] and d.__len__() >= 2:
                        if d[k] in op and d[k] == d[k-1]:
                            print("==============================")
                            m[len(m)-1], c = operators(m[len(m)-1], m[j - 1], m[j])
                            n[0] = m[len(m)-1]
                            k = k - 1
                            j = j - 1
                            op.remove(c)
                            if k <= 0:
                                break
                        elif d[k] in op and op.__len__() != 1 and d[k] != d[k-1]:
                            pt = min(symbol[d[k]], symbol[d[k-1]])
                            sd = [key1 for key1, value in symbol.items() if value == pt]
                            j = m.index(sd[0])
                            m[j - 1], c = operators(m[j - 1], m[j + 1], m[j])
                            n[0] = m[j - 1]
                            k = k - 1
                            j = j - 1
                            op.remove(c)
                            print("###########outside############", j)
                            if k <= 0:
                                break
                        elif (not d[k] in op) and (d[k-1] in op):
                            pt = max(symbol[d[k]], symbol[d[k - 1]])
                            sd = [key1 for key1, value in symbol.items() if value == pt]
                            j = m.index(sd[0])
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", sd[0])
                            m[j + 1], c = operators(m[j - 1], m[j + 1], m[j])
                            n[0] = m[j + 1]
                            k = k - 1
                            j = j - 1
                            op.remove(c)
                            if k <= 0:
                                break
                        if op.__len__() == 0:
                            break
                        else:
                            print(f"-----------------------------------", {k})
                        k = k - 1
                        print(n[0])
                        break
                    elif m[j] == d[k] and d.__len__() == 1:
                        print("###########______elif______############", j)
                        m[j + 1], c = operators(m[j + 1], m[j - 1], m[j])
                        n[0] = m[j + 1]
                        j = j + 1
                        op.remove(c)
                        k = k - 1
                        if op.__len__() == 0:
                            break
                        break
                    elif m[j] != d[k] and d.__len__() >= 1:
                        j = j - 1
                        if j <= 0 and op.__len__() == 0:
                            print("------?------")
                            j = 0
                            #k = k - 1
                    if op.__len__() == 0:
                        break
                #print(n[0])
                if k <= 0:
                    break
                # ------------------------------------------

        if p == x.__len__():
            break

    if isinstance(n[0], float):
        print(f"Final Result is: {n[0]}")
        return output()
    elif isnumeric(in1):
        for s in range(0, x.__len__()):
            n[0] = n[0] + x[s]
            s = s + 1
        print("Final Single Output is:", n[0])
        return output()
    elif in1 == "c":
        print("-----EXIT-----")
    else:
        print("Error")
        return output()


if __name__ == "__main__":
    print_output()
