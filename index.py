import CharacterCreator
import NewAttack

print("Jim's Rolemaster Stuff")

EXIT_INPUT = 0
choices = [
    {"num": "1", "text": "Attack With Hotkeyed Char 1"},
    {"num": "7", "text": "Create Character"},
    {"num": "8", "text": "Select Character"},
    {"num": "9", "text": "List Character"},
    {"num": "0", "text": "Exit"}
]
validChoices = { "1", "2", "3", "4", "7", "8", "9", "0" }
hotKeyCharacters = []

while(True):
    for option in choices:
        print( option["num"] + " : " + option["text"])
    
    choice = input()

    if choice not in validChoices:
        print("not a valid choice")
    
    if choice == "1":
        char1 = hotKeyCharacters[0]
        char2 = hotKeyCharacters[1]
        char1.attack(char2)
    elif choice == "7":
        character = CharacterCreator.genChar()
        if len(hotKeyCharacters) <= 4:
            hotKeyCharacters.append(character)
    elif choice == "0":
        break
