#look for sections
#look for units
#add weapons
#new line means new unit


def removeGroup(str, beg, end):
    sw = (str + '.')[:-1]
    result = ""
    while sw.find(beg) != -1:
        a = str.find(beg)
        b = str.find(end)
        result += sw[:a]
        sw = sw[b+1:]
    result += sw
    return result

#stop lines
y = ["CHARACTERS", "OTHER DATASHEETS", "EPIC HERO"]


#open army list file
imp = input("Army List> ")
with open("./ArmyLists/"+imp, "r") as f:
    x = f.read().split("\n\n")
modelSheets = []
with open("./Data/Models.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        modelSheets+=[l.split(",")]

#start after the first stop word
i = 0
while i < len(x):
    if x[i].strip() == "CHARACTERS" or x[i].strip() == "OTHER DATASHEETS":
        i+=1
        break
    i+=1

#iterate through 
while i < len(x):
    if x[i].strip() in y:
        i+=1
        continue
    for j in x[i]:
        j = removeGroup(j, "(", ")")
        j = j.strip()

        for m in modelSheets:
            if m[2].upper() == j.upper():
                found = True
                id = int(m[0])
                break
        print()

    i+=1