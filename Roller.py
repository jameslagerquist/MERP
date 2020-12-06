import random
def roll1d100():
    roll = random.randrange(1, 100)
    print("Raw Dice Roll:" + str(roll))
    return roll