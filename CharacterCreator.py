import random
import json
import dataStore.CharacterNames
from dataStore.weapon import rollDamageTable
from Roller import roll1d100

def roll1d100String():
    return random.randrange(20, 100)

class Character:
    def __init__(self, name: str):
        self.name = name
        self.stats = dict()
        self.cclass = str()
        self.OB = 0
        self.DB = 0
        self.weapon = "2hweap"
        self.armor = "Chain"
        self.crace = "Undefined"

    def chooseClass(self):
        classes = ["Warrior", "Ranger", "Mage", "Animist", "Scout", "Bard"]
        self.cclass = random.choice(classes)

    def chooseRace(self):
        races = ["Hobbit", "Umli", "Dwarf", "Wose", "Urban Man", "Dunedain", "Half-Elf", "Silvan Elf", "Sindar Elf", "Noldor Elf",
                 "Half-Orc", "Orc", "Uruk-hai", "Half-Troll", "Troll", "Olog-hai", "Rural Man", "Rohir", "Beorning",
                 "Woodman", "Dorwinadan", "Lossadan", "Dunlending", "Easterling", "Haradan", "Corsair", "Variag", "Black Numenorean"]
        self.crace = random.choice(races)

    def chooseRandomArmor(self):
        armors = ["Plate", "Chain", "Rigid Leather", "Soft Leather", "None"]
        self.armor = random.choice(armors);
    
    def chooseRandomWeapon(self):
        weaponTypes = ["slash", "concussion", "2hweap", "missle"]
        self.weapon = random.choice(weaponTypes)

    def prettyPrintJson(self):
        print("--- Stats Sheet for " + self.name + " The " +
              self.crace + " " + self.cclass + "---")
        for key in self.stats:
            print(key + " - " + str(self.stats[key]))
        print("-------------------------------------\n")

    def rollStats(self):
        self.stats["strength"] = roll1d100String()
        self.stats["agility"] = roll1d100String()
        self.stats["constitution"] = roll1d100String()
        self.stats["intelligence"] = roll1d100String()
        self.stats["intuition"] = roll1d100String()
        self.stats["presence"] = roll1d100String()
        self.stats["appearance"] = roll1d100String()

    def adjustStat(self, statName: str, amount: int):
        isString = isinstance(statName, str)
        self.stats[statName.lower()] += amount
    def setOb(self, amount: int):
        self.OB = amount
    def setDb(self, amount: int):
        self.DB = amount
    def attack(self,enemy):
        roll = roll1d100()
        rollDamageTable(roll, self.weapon, enemy.armor)
    def setArmor(self,arm):
        self.armor = arm
    def setWeapon(self,weap):
        self.weapon = weap

def genChar():
    newChar = Character(dataStore.CharacterNames.generateName())
    newChar.rollStats()
    newChar.chooseRandomArmor()
    newChar.chooseRandomWeapon()
    newChar.chooseRace()
    newChar.chooseClass()
    newChar.prettyPrintJson()
    return newChar