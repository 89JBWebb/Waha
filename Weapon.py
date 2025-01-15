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

    kw = []
    if len(i[5]) != 0:
        for k in i[5].split(","):
            start = k.find(">")
            stop = k.find("</")
            kw+=[k[start+1:stop].upper()]
    return Weapon(a, b, int(i[-4]), abs(int(i[-3])), c, kw)

class Weapon:

    def __init__(self, attacks, BWS, strength, AP, damage, kwargs):
        self.attacks = attacks
        self.BWS = BWS
        self.strength = strength
        self.AP = AP
        self.damage = damage

        self.keys = {}

        for k in kwargs:
            if any(char.isdigit() for char in k):
                ls = k.rindex(' ')
                self.keys[k[:ls]] = int(k[ls:])
            else:
                self.keys[k] = 1
        print(self.keys)