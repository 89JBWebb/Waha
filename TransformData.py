necronIds = []

with open("./Data/Datasheets.csv", encoding="utf8") as f:
    for l in f:
        if l.split("|")[2] == "NEC":
            necronIds+= [int(l.split("|")[0])]

print(necronIds)

with open("./Data/Necron Weapons.txt", "w") as g:
    '''with open("./Data/Datasheets_models.csv", encoding="utf8") as f:
        next(f)
        for l in f:
            if int(l.split(",")[0]) in necronIds:
                g.write(l)'''

    with open("./Data/Datasheets_wargear.csv", encoding="utf8") as f:
        next(f)
        for l in f:
            if len(l.split(",")[0])!= 0:
                if int(l.split(",")[0]) in necronIds:
                    for i in [0, 1, 4]:
                        g.write(l.split(",")[i].strip())
                        g.write(",")
                    
                    s = l.split(",")[5].strip()
                    if "<" in s:
                        a = s.find(">")
                        b = s.find("</")
                        g.write(s[a+1:b])
                        s = s[b+1:]
                    g.write(",")

                    s = l.split(",")[6].strip()
                    if "<" in s:
                        a = s.find(">")
                        b = s.find("</")
                        g.write(s[a+1:b])
                        s = s[b+1:]
                    g.write(",")
                    
                    for i in [7, 8, 9, 10, 11, 12]:
                        g.write(l.split(",")[i].strip())
                        g.write(",")
                    g.write("\n")