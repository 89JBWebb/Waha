import random as r

'''def roll(n, lookingFor):
    counter = 0
    counter6 = 0
    print(lookingFor, end=": ")
    for i in range(0,n):
        x = r.randint(1,6)
        print(x, end=" ")
        if x == 6:
            counter6+=1
            counter+=1
        elif x >= lookingFor:
            counter+=1
    print()
        
    return [counter, counter6]'''

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

    def __init__(self, models, toughness, save, wounds):
        self.models = models
        self.toughness = toughness
        self.save = save
        self.wounds = wounds
        self.allocated = wounds

    '''def melee(self, weapon, victim):
        a = roll(self.models*weapon.attacks, weapon.BWS)
        
        if weapon.lethalHits:
            b = roll(a[0]-a[1], toWound(weapon.strength, victim.toughness))
        else:
            b = roll(a[0], toWound(weapon.strength, victim.toughness))
        if weapon.lethalHits:
            c = roll(b[0]+a[1], victim.save+weapon.AP)
        else:
            c = roll(b[0], victim.save+weapon.AP)
        if weapon.lethalHits:
            victim.allocate(weapon.damage, a[1]+b[0]-c[0])
        else:
            victim.allocate(weapon.damage, b[0]-c[0])'''
    
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
        return str(self.models)

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

immortals = Unit(5,5,3,1)
immortals2 = Unit(5,5,3,1)
gaussBlaster = Weapon(2,3,5,1,1, lethalHits=True)
teslaCarbine = Weapon(2,3,5,0,1, sustainedHits=2)

print(immortals)
immortals2.ranged(teslaCarbine, immortals, verbose=True)
print(immortals)
