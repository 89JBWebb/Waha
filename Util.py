#defines utility methods to be used otherwhere in the project

import random as r

def getInput():
    try:
        imp = input("> ")
    except EOFError:
        imp = input("> ")
    return imp


def roll(imp, **kwargs):
    result = 0
    if "D" in imp.upper():
        d = imp.upper().find("D")
        if d == 0:
            rolls = 1
        else:
            rolls = int(imp[:d])
        if "+" in imp:
            plus = imp.find("+")
            result += int(imp[plus+1:])
            for i in range(rolls):
                x = r.randint(1, int(imp[d+1:plus]))
                if "verbose" in kwargs:
                    print(x, end=" ")
                result += x
        else:
            for i in range(rolls):
                x = r.randint(1, int(imp[d+1:]))
                if "verbose" in kwargs:
                    print(x, end=" ")
                result += x
    return result

def toWound(s,t):
    if s >= t*2:
        return 2
    elif s > t:
        return 3
    elif s == t:
        return 4
    elif s*2 <= t:
        return 6
    return 5

def aver(x):
    if type(x) == int:
        return x
    if "D" in x.upper():
        d = x.upper().find("D")
        plus = x.find("+")

        if plus == -1:
            c = 0
            plus = len(x)
        else:
            c = int(x[plus+1:])

        if d == 0:
            a = 1
        else:
            a = int(x[:d])

        b = int(x[d+1:plus])

        result = a*(b+1)/2+c

        return a*(b+1)/2+c

    return x