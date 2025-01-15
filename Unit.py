from Util import roll, toWound
import random as r

class Unit:

    created = 0

    def __init__(self, name, models, rangedWeapons, meleeWeapons, toughness, save, wounds):
        self.models = models
        self.fullStrength = models
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
        attacks = 0
        if isinstance(weapon.attacks, str):
            if "verbose" in kwargs:
                print("\ntacks " + weapon.attacks + ": ", end="")
            for i in range(self.models):
                attacks += roll(weapon.attacks, verbose = True)
            print()
        else:
            attacks = self.models*weapon.attacks
    
        hits = 0
        wounds = 0
        rerollWounds = 0
        notSaved = 0

        if weapon.blast:
            attacks += int(victim.models/5)*self.models
        if not weapon.torrent and weapon.BWS >= 2:
            if "verbose" in kwargs:
                print("\nto hit ", end="")
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
        else:
            hits+=attacks
        
        if "verbose" in kwargs:
            print("wounds ", end="")
            print(toWound(weapon.strength, victim.toughness), end=": ")
        for i in range(hits):
            x = r.randint(1,6)
            if "verbose" in kwargs:
                print(x, end=" ")
            if x == 6 and weapon.devastatingWounds:
                notSaved+=1
            elif x >= toWound(weapon.strength, victim.toughness):
                wounds+=1
            elif weapon.twinLinked:
                rerollWounds+=1
        if "verbose" in kwargs:
            print()

        if rerollWounds != 0:
            if "verbose" in kwargs:
                print("reroll wounds ", end="")
                print(toWound(weapon.strength, victim.toughness), end=": ")
            for i in range(rerollWounds):
                x = r.randint(1,6)
                if "verbose" in kwargs:
                    print(x, end=" ")
                if x == 6 and weapon.devastatingWounds:
                    notSaved+=1
                elif x >= toWound(weapon.strength, victim.toughness):
                    wounds+=1
            if "verbose" in kwargs:
                print()

        if victim.save+weapon.AP <= 6:
            if "verbose" in kwargs:
                print("saves  ", end="")
                print(victim.save+weapon.AP, end=": ")
            for i in range(wounds):
                x = r.randint(1,6)
                if "verbose" in kwargs:
                    print(x, end=" ")
                if x < victim.save+weapon.AP:
                    notSaved+=1
            if "verbose" in kwargs:
                print()
        else:
            notSaved = wounds

        if isinstance(weapon.damage,str):
            for i in range(notSaved):
                victim.allocate(roll(weapon.damage), 1)
        else:
            victim.allocate(weapon.damage, notSaved)
        
        if weapon.hazardous:
            if "verbose" in kwargs:
                print("hazard 2: ", end="")
            for i in range(self.models):
                x = r.randint(1,6)
                if "verbose" in kwargs:
                    print(x, end=" ")
                if x == 1:
                    if self.fullStrength == 1:
                        self.allocate(1, 3)
                    else:
                        self.pull()
            if "verbose" in kwargs:
                print()


    def allocate(self, damage, times):
        for i in range(times):
            self.allocated-=damage
            if self.allocated <= 0:
                self.models-=1
                self.allocated = self.wounds
    
    def pull(self):
        self.models-=1
        self.allocated = self.wounds

    def __str__(self):
        return str(self.number)+" "+self.name+" "+str(self.models)+" ("+str(self.allocated)+")"
