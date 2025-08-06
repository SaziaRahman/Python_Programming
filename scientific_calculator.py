import operator

from numpy.core.defchararray import isnumeric

i = 1
c = 1
ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul,
       "%": operator.mod, "^": operator.pow}
while i == 1:
    op = {"0": "", "1": "", "2": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}
    Res = input("Start:")
    j = p = m = 0

    opt = [p for p in Res if p == "+" or p == "-" or p == "/" or p == "*" or p == "%" or p == "^"]
    print(opt)
    for j in range(len(Res)):
        for m in range(len(opt)):
            j = Res.index(opt[m])
            q = j + 1
            op["1"] = opt[m]
            g = q
            f = len(Res)
            for p in range(len(Res)):
                if Res[p] == "(":
                    Res0 = Res[p + 1:j]
                    op["0"] = op["0"] + str(Res0)
                else:
                    Res0 = Res[:j]
                    op["0"] = op["0"] + str(Res0)
                break
            for p in reversed(Res):
                if p == ")":
                    n = len(opt)
                    if n > 1:
                        for r in range(g, f):
                            for b in range(len(opt[m: n])):
                                print(b)
                                if Res[r] == opt[b]:
                                    while b < n - 1:
                                        b = b + 1
                                    cg = Res.index(p)
                                    print("Clear1:", r)
                                    op["2"] = str(Res[g:r])
                                    if "(" in op["2"]:
                                        op["2"] = Res[(Res.index("(") + 1):r]
                                    elif ")" in op["2"]:
                                        op["2"] = Res[g: Res.index(")")]
                                    op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                                    op["1"] = Res[r]
                                    g = r + 1

                                    if r < g:
                                        r = r + 1

                                    if b == n - 1:
                                        print("deep02", Res[g:cg], b)
                                        op["2"] = str(Res[g:cg])
                                        print(op["0"], op["2"], op["1"])
                                        break
                                    elif b + 1 < n:
                                        print("deep03", Res[g:], b)
                                        continue
                                    print("deep_b", b)
                                    print("if")
                        op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                        break
                    else:
                        print("Clear01:")
                        pg = Res.index(p)
                        Res2 = Res[q:pg]
                        op["2"] = op["2"] + str(Res2)
                        op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                    break

                elif ")" not in Res:
                    n = len(opt)
                    if n > 1:
                        for r in range(g, f):
                            for b in range(len(opt[m: n])):
                                print(b)
                                if Res[r] == opt[b]:
                                    while b < n - 1:
                                        b = b + 1
                                    print("deep",b)
                                    op["2"] = str(Res[g:r])
                                    print(op["0"], op["2"], op["1"])
                                    op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                                    op["1"] = Res[r]
                                    g = r + 1

                                    if r < g:
                                        r = r + 1

                                    if b == n-1:
                                        print("deep02", Res[g:], b)
                                        op["2"] = str(Res[g:])
                                        print(op["0"], op["2"], op["1"])
                                        break
                                    elif b + 1 < n:
                                        print("deep03", Res[g:], b)
                                        continue
                                    #b = b + 1
                                    print("deep_b", b)
                                    print("if")
                                #break
                                #b = b + 1
                        print("DEEP", op["0"], op["2"], op["1"])
                        op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                    else:
                        print("Clear03:")
                        Res2 = Res[q:]
                        op["2"] = op["2"] + str(Res2)
                        op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                    break

                elif isnumeric(Res[Res.index(")") + 1]):
                    pg = Res.index(")")
                    ResD = Res[:pg]
                    opt1 = [p for p in ResD if p == "+" or p == "-" or p == "/" or p == "*" or p == "%" or p == "^"]
                    n = len(opt1)
                    if n > 1:
                        for r in range(g, f):
                            if m + 1 < n:
                                # print(m)
                                if Res[r] == opt[m + 1]:
                                    print("ClearS:", r)
                                    op["2"] = str(Res[g:r])
                                    if "(" in op["2"]:
                                        op["2"] = Res[(Res.index("(") + 1):r]
                                    elif ")" in op["2"]:
                                        op["2"] = Res[g: Res.index(")")]
                                    op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                                    g = r + 1
                                    op["2"] = str(Res[g:pg])
                                    op["1"] = Res[r]
                                    op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                                    print(range(pg + 1, len(Res)))
                                    op["2"] = str(Res[pg + 1:])
                                    for k in range(pg + 1, len(Res)):
                                        if Res[k] == "+" or Res[k] == "-" or Res[k] == "/" or Res[k] == "*" or Res[k] == "^" or Res[k] == "%":
                                            op["2"] = str(Res[pg + 1:k])
                                            op["1"] = Res[k]
                                            print("if")
                                            break
                                        else:
                                            op["1"] = ""
                                            continue
                                    print(range(pg + 1, len(Res)))
                                    op["0"] = str(ops["*"](int(op["0"]), int(op["2"])))
                                    if op["1"] == "+" or op["1"] == "-" or op["1"] == "/" or op["1"] == "*" or op["1"] == "^" or op["1"] == "%":
                                        continue
                                    else:
                                        op["1"] = "*"
                                        op["2"] = "1"
                                        break

                        print(op["0"], op["2"], op["1"])
                        #op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                        break
                    else:
                        op["2"] = str(Res[g:pg])
                        if "(" in op["2"]:
                            op["2"] = Res[(Res.index("(") + 1):pg]
                        elif ")" in op["2"]:
                            op["2"] = Res[g: Res.index(")")]
                        op["0"] = str(ops[op["1"]](int(op["0"]), int(op["2"])))
                        op["2"] = str(Res[pg + 1:])
                        for k in range(pg + 1, len(Res)):
                            if Res[k] == "+" or Res[k] == "-" or Res[k] == "/" or Res[k] == "*" or Res[k] == "^" or Res[k] == "%":
                                op["2"] = str(Res[pg + 1:k])
                                op["1"] = Res[k]
                                print(op["0"], op["2"], op["1"])
                                print("if")
                                break
                            else:
                                continue
                        op["0"] = str(ops["*"](int(op["0"]), int(op["2"])))
                        break

            m = m+1
            break
        print(op["0"], op["2"], op["1"])
        print("Result: ", op["0"])
        break

    i = int(input('''Choose an option:
                    (1) Continue the loop
                    (2) exit
                    Enter between 1 & 2:'''))
