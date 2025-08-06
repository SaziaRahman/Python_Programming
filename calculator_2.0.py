from numpy.core.defchararray import isnumeric


def print_output():
    try:
        print("Calculator Input:\n", end="")
        Calculator_input = output()
        operation(Calculator_input)
    except TypeError:
        pass


def output():
    while True:
        try:
            in1 = input('''=============================\n(Enter 'c' to exit)\n-----Start-----:''')
            if in1 == "":
                continue
            elif in1 == "c":
                print(f'''<<<<<EXIT>>>>>''')
                print('''=============================''')
                return 0
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
            print(f'''Operation Failed''')
    except TypeError:
        pass
    return a, b, d


def get_key(dictionary):
    for key, value in dictionary.items():
        return key


def operation(in1):
    y = in1
    n = ["", ""]
    b = ""
    op = []
    c = ""
    l, f = 0, 0
    m = []
    x = [a := i if i in range(1, 11) else i for i in y]
    symbols = {1: "^", 2: "*", 3: "/", 4: "-", 5: "+", 6: "%"}
    for i in x:
        if i == "(":
            x.remove("(")
        if i == ")":
            x.remove(")")

    in1 = ""
    for i in x:
        in1 = in1 + i

    for i in in1:
        for key, v in symbols.items():
            if i == v:
                op.append(v)
    symbol_ops = []
    for i in op:
        for key in symbols:
            if i == symbols[key]:
                symbol_op = {key: symbols[key]}
                symbol_ops.append(symbol_op)
    d = []
    for s in sorted(symbol_ops, key=get_key):
        for k, v in s.items():
            d.append(v)

    for i in d:
        if i == d[f]:
            num1 = in1.split(i)
            if d.__len__() > 1:
                if f == len(op):
                    break
                if d[f+1] in num1[f]:
                    num2 = num1[f].split(d[f+1])
                    for r in range(f, num2.__len__()-1):
                        m.append(num2[r])
                        m.append(d[r+1])
                    m.append(num2[num2.__len__()-1])
                else:
                    num5 = num1[0].split(d[f - 1])
                    for r in range(f, num5.__len__() - 1):
                        m.append(num5[r])
                        m.append(d[r - 1])
                    m.append(num5[num5.__len__() - 1])
            else:
                m.append(num1[f])
            m.append(i)
            if f == len(op):
                break
            if d.__len__() > 1:
                if d[f + 1] in num1[f + 1]:
                    num3 = num1[f + 1].split(d[f + 1])
                    m.append(num3[f])
                    m.append(d[f + 1])
                    m.append(num3[f+1])
                else:
                    for r in range(f+1, num1.__len__()-1):
                        m.append(num1[r])
                        m.append(d[r])
                    m.append(num1[num1.__len__()-1])
                    break
            else:
                m.append(num1[f+1])
        break
    print('''-----------<<x>>-------------''')
    l = 0
    p = len(m) - 1
    while p >= 0 and len(m) > 2:
        if m[p] == d[l]:
            if m[p-2] == "-":
                m[p-1] = "-" + m[p-1]
            n[1], n[0], c = operators(m[p - 1], m[p + 1], m[p])
            l = l + 1
            if l == len(d):
                break
            if p == 1:
                p = len(m) - 1
                if n[1] < 0:
                    n[1] = -n[1]
                m[p - 2] = n[1]
            else:
                if n[1] < 0 and m[p-2] == "-":
                    n[1] = -n[1]
                m[p - 1] = n[1]
        p = p - 1

    if isinstance(n[1], float):
        print(f'''<<< Final Result is: {n[1]} >>>''')
        print('''=============================''')
        return output()
    elif isnumeric(in1):
        for s in range(0, x.__len__()):
            n[0] = n[0] + x[s]
            s = s + 1
        print(f'''<<< Final Single Output is: {n[0]} >>>''')
        print('''=============================''')
        return output()
    elif in1 == "c":
        print(f'''<<<<<EXIT>>>>>''')
        print('''=============================''')
        return 0
    else:
        print(f'''Error''')
        return output()


if __name__ == "__main__":
    print_output()
