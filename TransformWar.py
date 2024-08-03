with open("./Data/Weapons.txt", "w") as f:
    with open("./Data/Datasheets_wargear.csv", "r") as g:
        for l in g:
            while "<" in l:
                a = l.find("<")
                f.write(l[:a])
                b = l.find(">")
                c = l.find("</")
                f.write(l[b+1:c])
                l = l[c:]
                d = l.find(">")
                l = l[d+1:]
            f.write(l)