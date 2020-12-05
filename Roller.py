import random
def roll1d100():
    roll = random.randrange(1, 100)
    print("Rolled:" + str(roll))
    return roll