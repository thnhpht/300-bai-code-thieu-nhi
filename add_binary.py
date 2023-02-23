def addBinary(a, b):
    carry_over = False
    res = ""

    if len(a) > len(b):
        for i in range(len(a) - len(b)):
            b = "0" + b
    elif len(b) > len(a):
        for i in range(len(b) - len(a)):
            a = "0" + a

    while a != "":
        if a[-1:] != b[-1:]:
            if carry_over:
                res = "0" + res
            else:
                res = "1" + res
                carry_over = False
        else:
            if a[-1:] == "0":
                if carry_over:
                    res = "1" + res
                else:
                    res = "0" + res
                carry_over = False
            else:
                if carry_over:
                    res = "1" + res
                else:
                    res = "0" + res
                carry_over = True
        a, b = a[:-1], b[:-1]

    if carry_over:
        return "1" + res
    return res

a = "11"
b = "1"
print(addBinary(a, b))
