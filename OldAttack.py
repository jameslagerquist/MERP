import random

attOB = int(input("What is the Attacker's OB? "))
#attWE = input("What is the Attacker's Weapon/Attack? ") NEED CODE
defDB = int(input("What is the Defender's DB? "))
#defAT = input("What is the Defender's Armor Type? ") NEED CODE

weapons = {
    "da" : "Dagger",
    "ss" : "Short Sword",
    "fa" : "Falchion",
    "bs" : "Broadsword",
    "sc" : "Scimitar",
    "th" : "Two Handed Sword",
    "ma" : "Mace",
    "ha" : "Hand Axe",
    "wh" : "War Hammer",
    "ba" : "Battle Axe",
    "wm" : "War Mattock",
    "cl" : "Club",
    "qs" : "Quarterstaff",
    "sp" : "Spear",
    "ml" : "Mounted Lance",
    "ja" : "Javelin",
    "pa" : "Pole Arm",
    "sl" : "Sling",
    "cp" : "Composite Bow",
    "sb" : "Short or Horse Bow",
    "lb" : "Long Bow",
    "lcb" : "Light Crossbow",
    "hcb" : "Heavy Crossbow",
    "bo" : "Bola",
    "wp" : "Whip",
    "ts" : "Throwing Star",
    "hb" : "Halbard",
    "ro" : "Rock",
    "pi" : "Pincher/Beak",
    "bi" : "Bite",
    "cl" : "Claw/Talon",
    "ho" : "Horn/Tusk/Stinger",
    "gr" : "Grapple/Grasp/Envelope/Swallow",
    "ra" : "Ram/Butt/Bash/Slug",
    "ti" : "Tiny Animals",
    "st" : "Stomp/Trample",
    "fall" : "Fall/Crush",
    "fi" : "Fist/Kick",
    "wr" : "Wrestling/Tackles",
}

armor = {
    "no" : "None",
    "sl" : "Soft Leather",
    "rl" : "Rigid Leather",
    "ch" : "Chain",
    "pl" : "Plate"
}

def attackroll():
    attack = random.randrange(1, 100)
    attack2 = random.randrange(1, 100)
    fumble = random.randrange(1, 100)
    crit1 = random.randrange(1,100)
    crit2 = random.randrange(1,100)

    if attack in range (96,100):
        print("You rolled an open ended number! Rolling again. ")
        print("First Roll = ")
        print(attack)
        print("Second Roll = ")
        print(attack2)
        print("Total = ")
        print(attOB + attack + attack2 - defDB)
    elif attack in range (1,8):
        print("Oh no! You may have fumbled! ")
        print("Here is the initial roll. ")
        print(attack)
        print("Here is the fumble roll. ")
        print(fumble)
        print("Here is the original attack total. ")
        print(attOB + attack - defDB)
    elif attack == 69:
        print("You rolled a 69 Dude! That becomes 96. Rolling again. ")
        print(attOB + 96 + attack2 - defDB)
    elif attack == 66:
        print("You rolled a 66! That becomes 99. Rolling again. ")
        print(attOB + 99 + attack2 - defDB)
    else:
        print("The total is ")
        print(attOB + attack - defDB)
    print("Your first crit roll is: " + str(crit1))
    print("Your second crit roll is: " + str(crit2))

#total = attackroll()
#attweapon = weapons.get("da")
print("----------")
print(attackroll())
print("----------")
