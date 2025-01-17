from Util import avg, toWound

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
                self.keys[k[:ls]] = k[ls:]
            else:
                self.keys[k] = 1
    
    def score(self, T, SV):
        a = 7-self.BWS
        b = 7-toWound(self.strength, T)
        c = min(7-SV+self.AP,6)
        result = a * b * c
        if "LETHAL HITS" in self.keys:
            result -= b * c
            result += 6 * c
        if "DEVASTATING WOUNDS" in self.keys:
            result -= a * c
            result += 6 * a
        if "TWIN-LINKED" in self.keys:
            result += (6-b)*b*a*c/6
        return round(result,1)
    
    def wscore(self, T, SV, W):
        return round(self.score(T, SV)/216.0 * avg(self.attacks) * min(avg(self.damage), W), 2)
    
    def __str__(self):
        return self.name + "\t" + str(self.attacks) + "\t" + str(self.BWS) + "\t" + str(self.strength) + "\t" + str(self.AP) + "\t" + str(self.damage) + "\t" + str(self.keys)
