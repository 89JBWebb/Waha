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
        ac = 1
        bc = 1
        if "+1 TO HIT" in self.keys and a < 5:
            a += 1
        if "HEAVY" in self.keys and a < 5:
            a += 1
        if "5+ CRITS" in self.keys:
            ac += 1
        if "RE-ROLL TO HIT" in self.keys:
            a  += a  * (6-b) / 6
            ac += ac * (6-b) / 6
        elif "RE-ROLL 1S TO HIT" in self.keys:
            a  += a  / 6
            ac += ac / 6
        if "TWIN-LINKED" in self.keys:
            b  += b  * (6-c) / 6
            bc += bc * (6-c) / 6
        elif "TWIN-LINKED 1S" in self.keys:
            b  += b  / 6
            bc += bc / 6
        if "SUSTAINED HITS" in self.keys:
            a += self.keys["SUSTAINED HITS"] * ac
        result = a * b * c
        if "LETHAL HITS" in self.keys:
            result += (6 - b) * ac * c
        if "DEVASTATING WOUNDS" in self.keys:
            result += (6 - c) * bc * a
        return result
    
    def wscore(self, T, SV, INV, W):
        result = self.score(T, SV, INV)/216.0 * aver(self.attacks) * min(aver(self.damage), W)
        return result

    def addKW(self, kw):
        self.keys[kw] = 1

    def __str__(self):
        return self.name + "\t" + str(self.attacks) + "\t" + str(self.BWS) + "\t" + str(self.strength) + "\t" + str(self.AP) + "\t" + str(self.damage) + "\t" + str(self.keys)
