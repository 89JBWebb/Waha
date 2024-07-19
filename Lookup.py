import random as r

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

class Unit:

    created = 0

    def __init__(self, name, models, rangedWeapons, meleeWeapons, toughness, save, wounds):
        self.models = models
        self.rangedWeapons = rangedWeapons
        self.meleeWeapons = meleeWeapons
        self.toughness = toughness
        self.save = save
        self.wounds = wounds
        self.allocated = wounds
        self.name = name
        Unit.created+=1
        self.number = Unit.created

    def melee(self, victim, **kwargs):
        for w in self.meleeWeapons:
            self.helper(w, victim, kwargs)

    def ranged(self, victim, **kwargs):
        for w in self.rangedWeapons:
            self.helper(w, victim, kwargs)

    def helper(self, weapon, victim, kwargs):
        attacks = self.models*weapon.attacks
        hits = 0
        wounds = 0
        notSaved = 0

        if "verbose" in kwargs:
            print(weapon.BWS, end=": ")
        for i in range(attacks):
            x = r.randint(1,6)
            if "verbose" in kwargs:
                print(x, end=" ")
            if weapon.sustainedHits != 0 and x == 6:
                hits+=1+weapon.sustainedHits
            elif weapon.lethalHits and x == 6:
                wounds+=1
            elif x >= weapon.BWS:
                hits+=1
        if "verbose" in kwargs:
            print()
        
        if "verbose" in kwargs:
            print(toWound(weapon.strength, victim.toughness), end=": ")
        for i in range(hits):
            x = r.randint(1,6)
            if "verbose" in kwargs:
                print(x, end=" ")
            if x >= toWound(weapon.strength, victim.toughness):
                wounds+=1
        if "verbose" in kwargs:
            print()
        if "verbose" in kwargs:
            print(victim.save-weapon.AP, end=": ")
        for i in range(wounds):
            x = r.randint(1,6)
            if "verbose" in kwargs:
                print(x, end=" ")
            if x < victim.save-weapon.AP:
                notSaved+=1
        if "verbose" in kwargs:
            print()

        victim.allocate(weapon.damage, notSaved)


    def allocate(self, damage, times):
        for i in range(times):
            self.allocated-=damage
            if self.allocated <= 0:
                self.models-=1
                self.allocated = self.wounds

    def __str__(self):
        return str(self.number)+" "+self.name+" "+str(self.models)

class Weapon:

    def __init__(self, attacks, BWS, strength, AP, damage, kwargs):
        self.attacks = attacks
        self.BWS = BWS
        self.strength = strength
        self.AP = AP
        self.damage = damage
        if "lethalHits" not in kwargs:
            self.lethalHits = False
        else:
            self.lethalHits = True
        if "sustainedHits" not in kwargs:
            self.sustainedHits = 0
        else:
            self.sustainedHits = 1


modelSheets = []
weaponSheets = []
with open("./Data/Necron Models.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        modelSheets+=[l.split(",")]
with open("./Data/Necron Weapons.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        weaponSheets+=[l.split(",")]
        weaponSheets[-1][0] = int(weaponSheets[-1][0])

fieldedUnits = []
imp = input("> ")
while imp != "quit":
    space = imp.find(" ")
    if imp[:space].upper() == "CREATE":
        imp = imp[space+1:]
        spacer = imp.rfind(" ")
        amount = int(imp[spacer+1:])
        outputMessage = "could not find what youre looking for"
        id = -1
        unitName = imp[:spacer]
        for m in modelSheets:
            if m[2].upper() == imp[:spacer].upper():
                outputMessage = m
                id = int(m[0])
                break
        print(outputMessage)
        
        potentialWeapons = []
        for w in weaponSheets:
            if w[0] == id:
                potentialWeapons += [w]
                print(w)

        imp = input("Ranged> ")
        while "E" in imp.upper():
            print("please type a number")
            imp = input("Ranged> ")
        rangedWeapons = imp.split()
        rwh = []
        for h in rangedWeapons:
            i = potentialWeapons[int(h)-1]
            print(i)
            rwh += [Weapon(int(i[6]), int(i[7]), int(i[8]), abs(int(i[9])), int(i[10]), [i[3],i[4]])]

        imp = input("Melee> ")
        while "E" in imp.upper():
            print("please type a number")
            imp = input("Ranged> ")
        meleeWeapons = imp.split()
        mwh = []
        for h in meleeWeapons:
            i = potentialWeapons[int(h)-1]
            mwh += [Weapon(int(i[6]), int(i[7]), int(i[8]), abs(int(i[9])), int(i[10]), [i[3],i[4]])]


        fieldedUnits += [Unit(unitName.lower(), amount, rwh, mwh, int(m[4]), int(m[5][:-1]), int(m[8]))]
        
    elif imp[:space].upper() == "RANGE":
        imp = imp[space+1:]
        si = imp.split()
        fieldedUnits[int(si[0])-1].ranged(fieldedUnits[int(si[1])-1], verbose=True)
    
    elif imp[:space].upper() == "MELEE":
        imp = imp[space+1:]
        si = imp.split()
        fieldedUnits[int(si[0])-1].melee(fieldedUnits[int(si[1])-1], verbose=True)

    elif imp.upper() == "LIST":
        for i in fieldedUnits:
            print(i)

    else:
        print("could not understand command")
    imp = input("> ")

for i in fieldedUnits:
    print(i)