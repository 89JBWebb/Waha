#look for sections
#look for units
#add weapons
#new line means new unit


def removeGroup(str, beg, end):
    sw = (str + '.')[:-1]
    if sw.find(beg) == -1:
        return sw
    result = ""
    while sw.find(beg) != -1:
        a = str.find(beg)
        b = str.find(end)
        result += sw[:a]
        sw = sw[b+1:]
    return result

y = ["CHARACTERS", "OTHER DATASHEETS"]

imp = input("Army List> ")
with open("./ArmyLists/"+imp, "r") as f:
    x = f.read().split("\n\n")

i = 0
while i < len(x):
    if x[i].strip() == "CHARACTERS" or x[i].strip() == "OTHER DATASHEETS":
        i+=1
        break
    i+=1
while i < len(x):
    if x[i].strip() in y:
        i+=1
        continue
    print(x[i])
    i+=1