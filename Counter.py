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

