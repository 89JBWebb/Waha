from Weapon import Weapon, weaponify

keywordSheets = []
modelSheets = []
weaponSheets = []
with open("./Data/Datasheets_keywords.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        keywordSheets+=[l.split("|")]
with open("./Data/Datasheets_models.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        modelSheets+=[l.split("|")]
        try:
            modelSheets[-1][0] = int(modelSheets[-1][0])
        except:
            modelSheets[-1][0] = -1
with open("./Data/Datasheets_wargear.csv", "r", encoding="utf8") as f:
    for l in f.readlines():
        weaponSheets+=[l.split("|")]
        try:
            weaponSheets[-1][0] = int(weaponSheets[-1][0])
        except:
            weaponSheets[-1][0] = -1

faction = "Necrons"
orkIds = []
orkWeapons = []
for line in keywordSheets:
    if line[1] == faction:
        orkIds += [int(line[0])]
for line in weaponSheets:
    if int(line[0]) in orkIds:
        orkWeapons += [weaponify(line)]
for w in orkWeapons:
    print(w.wscore(4,3,2), end=",")
    print(w.name)
