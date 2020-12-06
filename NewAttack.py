import random
from Roller import roll1d100
def attackroll(OB = 0, DB = 0):
    rollValue = roll1d100()
    totalRoll = rollValue

    while (checkRollforOpenEnded(rollValue)):
        rollValue = roll1d100()
        totalRoll += rollValue

    print("Roll Total was " + str(totalRoll))
    return (OB + totalRoll - DB)

def checkRollforOpenEnded(rollVal):
    if (rollVal == 69):
        return True
    if (rollVal ==66):
        return True
    if (rollVal >= 96):
        return True
    else:
        return False