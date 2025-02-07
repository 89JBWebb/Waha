from Unit import Unit
from Util import getInput, roll
from Weapon import weaponify

modelSheets = []
weaponSheets = []
with open("./Data/Datasheets_models.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        modelSheets+=[l.split("|")]
with open("./Data/Datasheets_wargear.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        weaponSheets+=[l.split("|")]
        try:
            weaponSheets[-1][0] = int(weaponSheets[-1][0])
        except:
            weaponSheets[-1][0] = -1

fieldedUnits = []
imp = getInput()
while imp != "quit":
    space = imp.find(" ")
    if imp[:space].upper() == "CREATE":
        imp = imp[space+1:]
        spacer = imp.rfind(" ")
        amount = int(imp[spacer+1:])
        found = False
        outputMessage = "could not find what youre looking for"
        id = -1
        unitName = imp[:spacer]
        for m in modelSheets:
            if m[2].upper() == imp[:spacer].upper():
                outputMessage = m
                found = True
                id = int(m[0])
                break
        print(outputMessage)

        if found:        
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
                rwh += [weaponify(i)]

            imp = input("Melee> ")
            while "E" in imp.upper():
                print("please type a number")
                imp = input("Ranged> ")
            meleeWeapons = imp.split()
            mwh = []
            for h in meleeWeapons:
                i = potentialWeapons[int(h)-1]
                mwh += [weaponify(i)]

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

    elif imp[:space].upper() == "ROLL":
        imp = imp[space+1:]
        print(roll(imp))
    
    elif imp[:space].upper() == "DEAL":
        imp = imp[space+1:]
        si = imp.split()
        fieldedUnits[int(si[0])-1].allocate(1, int(si[1]))
    
    elif imp[:space].upper() == "ADD":
        imp = imp[space+1:]
        kw, unit, weap = imp.rsplit(' ', 2)
        unit = int(unit)-1
        weap = int(weap)-1
        fieldedUnits[unit].addKW(kw, weap)
        print(0)

    elif imp[:space].upper() == "COUNTER":
        imp = imp[space+1:]
        t, sv, inv, w = imp.rsplit(' ', 3)
        t = int(t)
        sv = int(sv)
        inv = int(inv)
        w = int(w)
        for u in fieldedUnits:
            print(u.name + " (r)\t"+ str(u.wscore(0, t, sv, inv, w)))
            print(u.name + " (m)\t"+ str(u.wscore(1, t, sv, inv, w)))

    else:
        print("could not understand command")
    imp = getInput()

for i in fieldedUnits:
    print(i)