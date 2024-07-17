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

    def __init__(self, name, models, toughness, save, wounds):
        self.models = models
        self.toughness = toughness
        self.save = save
        self.wounds = wounds
        self.allocated = wounds
        self.name = name
        Unit.created+=1
        self.number = Unit.created

    def ranged(self, weapon, victim, **kwargs):
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

    def __init__(self, attacks, BWS, strength, AP, damage, **kwargs):
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
            self.sustainedHits = kwargs["sustainedHits"]


x = []
y = []
with open("./Data/Necron Models.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        x+=[l.split(",")]
with open("./Data/Necron Weapons.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        y+=[l.split(",")]
        y[-1][0] = int(y[-1][0])

z = []
imp = input("> ")
while imp != "quit":
    space = imp.find(" ")
    if imp[:space].upper() == "CREATE":
        imp = imp[space+1:]
        spacer = imp.rfind(" ")
        amount = int(imp[spacer+1:])
        a = "could not find what youre looking for"
        id = -1
        for m in x:
            if m[2].upper() == imp[:spacer].upper():
                a = m
                id = int(m[0])
                break
        print(a)
        for w in y:
            if w[0] == id:
                print(w)
        
        

        z += [Unit(imp[:spacer].lower(), amount, int(m[4]), int(m[5][:-1]), int(m[8])) ]
        
    elif imp[:space].upper() == "ATTACK":
        imp = imp[space+1:]
        print("attack!!!")
    else:
        print("could not understand command")
    imp = input("> ")

for i in z:
    print(i)