from Util import aver, toWound

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
    if i[-4].upper().find("D") != -1:
        d = i[-4]
    else:
        d = int(i[-4])

    kw = []
    if len(i[5]) != 0:
        for k in i[5].split(","):
            start = k.find(">")
            stop = k.find("</")
            kw+=[k[start+1:stop].upper()]
    return Weapon(i[4], a, b, d, abs(int(i[-3])), c, kw)

class Weapon:

    def __init__(self, name, attacks, BWS, strength, AP, damage, kwargs):
        self.name = name
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
    
    def score(self, T, SV, INV):
        a = 7-self.BWS
        b = 7-toWound(self.strength, T)
        c = min(SV+self.AP-1, 6, INV)
        result = a * b * c
        if "LETHAL HITS" in self.keys:
            result -= b * c
            result += 6 * c
        if "SUSTAINED HITS" in self.keys:
            result += self.keys["SUSTAINED HITS"] * b * c
        if "DEVASTATING WOUNDS" in self.keys:
            result -= a * c
            result += 6 * a
        if "TWIN-LINKED" in self.keys:
            result += (6-b)*b*a*c/6
        return result
    
    def wscore(self, T, SV, INV, W):
        result = self.score(T, SV, INV)/216.0 * aver(self.attacks) * min(aver(self.damage), W)
        return result

    def addKW(self, kw):
        self.keys[kw] = 1

    def __str__(self):
        return self.name + "\t" + str(self.attacks) + "\t" + str(self.BWS) + "\t" + str(self.strength) + "\t" + str(self.AP) + "\t" + str(self.damage) + "\t" + str(self.keys)
