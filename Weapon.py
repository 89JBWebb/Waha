def weaponify(i):
    if i[-6].upper().find("D") != -1:
        a = i[-6]
    else:
        a = int(i[-6])
    if i[-5] == "N/A":
        b = -1
    else:
        b = int(i[-5])
    if i[-2].upper().find("D") != -1:
        c = i[-2]
    else:
        c = int(i[-2])
    j = 5
    kw = []
    while i[j].upper() != "MELEE" and not i[j].isnumeric():
        start = i[j].find(">")
        stop = i[j].find("</")
        kw+=[i[j][start+1:stop]]
        j+=1
    return Weapon(a, b, int(i[-4]), abs(int(i[-3])), c, kw)

class Weapon:

    def __init__(self, attacks, BWS, strength, AP, damage, kwargs):
        self.attacks = attacks
        self.BWS = BWS
        self.strength = strength
        self.AP = AP
        self.damage = damage
        if "lethal hits" not in kwargs:
            self.lethalHits = False
        else:
            self.lethalHits = True
        if "sustained hits" not in kwargs:
            self.sustainedHits = 0
        else:
            self.sustainedHits = 1
        if "devastating wounds" not in kwargs:
            self.devastatingWounds = False
        else:
            self.devastatingWounds = True
        if "twin-linked" not in kwargs:
            self.twinLinked = False
        else:
            self.twinLinked = True
        if "blast" not in kwargs:
            self.blast = False
        else:
            self.blast = True
        if "torrent" not in kwargs:
            self.torrent = False
        else:
            self.torrent = True
        if "hazardous" not in kwargs:
            self.hazardous = False
        else:
            self.hazardous = True