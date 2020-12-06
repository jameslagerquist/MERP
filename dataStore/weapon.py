import json
relPath = "dataStore/"

def loadCritJson(fileName):
    with open(relPath + fileName) as json_file: 
        data = json.load(json_file)
        return data 

attackTables = {
    "slash" : loadCritJson("AT1_HandedSlash.json"),
    "concussion" : loadCritJson("AT2_1HandedConcussion.json"),
    "2hweap" : loadCritJson("AT3_2HandedWeapon.json"),
    "missle" : loadCritJson("AT4_MissileWeapons.json"),
}

def rollDamageTable(roll, weapType, enemyArm):
    global attackTables
    
    checkValidArmType(enemyArm)
    checkValidAttackType(weapType)

    if roll == None:
        raise Exception("[rollDamageTable]No roll value provided")
  
    attackTable = attackTables[weapType]
    damageReturn = None
    
    for attackObject in attackTable:
        if roll < attackObject["maxRoll"] or attackObject["maxRoll"] >= 150 and roll > attackObject["maxRoll"]:
            damageReturn = attackObject
            break
    oDmg = damageReturn[enemyArm]
    printAttackReport(oDmg, weapType, enemyArm, roll)
    return oDmg

def printAttackReport(oDmg, weapType, enemyArm, roll):
    print("--------------------------------")
    print("You rolled a " + str(roll) + " with a " + weapType + " attack against an enemy wearing " + enemyArm)
    dmg = oDmg['damage']
    if type(dmg) is not str:
        dmg = str(dmg)
    print ("Damage: " + dmg + " Critical: " + oDmg['crit'])
    print("--------------------------------")

def checkValidAttackType(attackType):
    validCritValues = ["slash", "concussion", "2hweap", "missle"]
    if attackType in validCritValues: 
        return True
    else:
        raise Exception("[rollDamageTable]Invalid roll type" + attackType + "provided")

def checkValidArmType(armType):
    validArmValues = ["Plate", "Chain", "Rigid Leather", "Soft Leather", "None"]
    if armType in validArmValues: 
        return True
    else:
        raise Exception("[rollDamageTable]Invalid roll type" + armType + "provided")
