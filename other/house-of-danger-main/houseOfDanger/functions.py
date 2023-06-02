import textwrap
import random
import json


dangerMeter = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 2, 2, 2]
dangDict = {'Water Bottle': (3, 'Discard at any time to lower Danger Meter by 3')}
psychDict = {}
climbDict = {}
fightDict = {'Pocketknife': (1, 'Increase Fighting roll by 1')}
dextDict = {}
percDict = {}
strengthDict = {}
items = {}
inv = {'danger': dangDict, 'psychic': psychDict, 'climbing': climbDict, 'fighting': fightDict, 'dexterity': dextDict,
       'perception': percDict, 'strength': strengthDict, 'items': items}


def inventory():
    for x in inv.items():
       for y in x:
              print(f'{y}: {x[y][1]}')
              print()


def wrap(text):
    form = textwrap.TextWrapper(width=100, initial_indent='  ')
    for x in text:
        for y in form.wrap(x):
            print(y)
        input()


def wrapFast(text):
    form = textwrap.TextWrapper(width=100, initial_indent='  ')
    for x in text:
        for y in form.wrap(x):
            print(y)
    input()


def choose(options):
    print("  Enter 'inv' to look at your inventory.")
    print()
    choice = input('  Your choice: ')

    while choice not in options and choice.lower() != 'inv':
        choice = input(f'Please enter {", ".join(options)}, or "inv": ')
    if choice.lower() == 'inv':
        inventory()
        while choice not in options:
            choice = input(f'Please enter {", ".join(options)}: ')
    print()
    return choice


def challenge(state, cat, danger):
    print(f'  Your Danger Level: {dangerMeter[danger]}')
    cont = True
    while state == 'optional':
        choice = input('Would you like to attempt this challenge? [y/n/inv] ')
        while choice.lower() not in ['y', 'n', 'inv']:
            choice = input("Please enter 'y' or 'n': ")
        if choice.lower() == 'inv':
            inventory()
        elif choice.lower() == 'n':
            print("  You did not attempt this challenge.")
            return 'quit'
        else:
            state = ''
    while cont:
        add = 0
        choice = ''
        while choice not in ['y', 'n']:
            choice = input('Would you like to check your inventory for an item to help you? [y/n] ')
        if choice == 'y':
            choices = list(inv[cat].keys()) + list(inv['danger'].keys())
            if len(choice) == 0:
                print('You have no items that can help!')
            else:
                for x in choices:
                    try:
                        print(x + ':', inv[cat][x][0])
                    except KeyError:
                        print(x + ': lower danger level by', inv['danger'][x][0], 'spaces')
                gear = ''
                choices.append('0')
                while gear not in choices:
                    gear = input('Enter the name of the item you would like to use or 0 for none:\nWARNING: If you roll'
                                 ' a 1 while using an item, you WILL lose the item!\n')
                if gear == '0':
                    choice = 'n'
                elif gear in dangDict.keys():
                    danger = dangerDown(danger, dangDict[gear][0])
                    del dangDict[gear]
                elif gear == 'Flashlight':
                    KO = OHKO()
                    if KO == 'empty':
                        choices.remove('Flashlight')
                        gear = ''
                    elif KO == 'cancel':
                        gear = ''
                    else:
                        return 'win', danger
                else:
                    add = inv[cat][gear][0]
                    choice = 'n'
        if choice == 'n':
            roll = random.randint(1, 6)
            if roll == 1:
                if add > 0:
                    del inv[cat][gear]
                    print(f"You rolled a one! You lost your {gear}")
                    return 'fail', danger
            elif dangerMeter[danger] > roll + add:
                print(f'You rolled a {roll}')
                return 'fail', danger
            else:
                print(f'You rolled a {roll}')
                return 'win', danger


def dangerUp(danger, psych, amount):
    danger += amount
    if danger > 9:
        psych = dePsych(psych, 2)
        danger = 2
        print("  You reach the top of the Danger Scale!")
        print(f"  Your Psychic Scale was set back by 2, and your Danger Level has been return to 3")
    else:
        print(f'  Your Danger Level is now {dangerMeter[danger]}. You are {9 - danger} spots away from the top of the '
              f'Danger Meter')
    return psych, danger


def dePsych(psych, amount):
    psych -= amount
    if psych < 1:
        psych = 1
    print(f'Your Psychic Scale is now at {psych}, and you are at {psychLevel(psych)}')
    return psych


def psychLevel(psych):
    if psych < 6:
        return 'Level 1'
    elif psych < 11:
        return 'Level 2'
    elif psych < 16:
        return 'Level 3'
    elif psych < 21:
        return 'Level 4'
    else:
        return 'Level 5'


def addInv(cat, name, description, amount=0):
    for x in inv:
        for y in x:
            if y == name:
                print('  You have already discovered this item.')
                return
    if cat == 'items':
        inv[cat][name] = description
    else:
        inv[cat][name] = (amount, description)


def psychUp(psych, amount):
    psych += amount
    if psych > 25:
        psych = 25
    print(f'Your Psychic Scale is now at {psych}, and you are at {psychLevel(psych)}')
    return psych


def dangerDown(danger, amount):
    danger -= amount
    if danger < 0:
        danger = 0
    print(f"  Your danger meter was lowered by {amount}. It is now at {dangerMeter[danger]}, with {9 - danger} spaces to"
          f" the top of the scale.")
    return danger


def OHKO():
    batteries = 0
    for x in items.keys():
        if x.split()[0].lower() == 'battery':
            batteries += 1
    if batteries == 0:
        print('You do not have any batteries!')
        return 'empty'
    else:
        print(f'  You have {batteries} batteries.')
        choice = input('  Would you like to use one to win this challenge? [y/n] ')
        while choice not in ['y', 'n']:
            choice = input("  Please enter 'y' or 'n': ")
        if choice == 'n':
            return 'cancel'
        else:
            for x in items.keys():
                if x.split()[0].lower() == 'battery':
                    items.pop(x)
                    break
            return 'win'


def save(psych, danger, chapter):
    name = input('Enter a name for your save file: ')
    name += '.json'
    data = {}
    for x in inv:
        data[x] = inv[x]
    data['final'] = (psych, danger, chapter)
    with open(name, 'w') as file:
        json.dump(data, file)
    print(f'{name} saved successfully!')


def loadSave():
    while True:
        try:
            file = input('Enter the name of your save file: ')
            if file[-5:] != '.json':
                file += '.json'
            saveFile = open(file, 'r')
            break
        except FileNotFoundError:
            print('File not found!')
            choice = input('Would you like to try again? [y/n] ')
            if choice == 'n':
                return 0, 0, 'cancel'
            else:
                pass
    data = json.load(saveFile)
    for x in data:
        if x != 'final':
            inv[x] = data[x]
        else:
            psych = data[x][0]
            danger = data[x][1]
            chapter = data[x][2]
    return psych, danger, chapter

"""
def opener():
    with Image.open('opener.jpg') as pic:
        print("  You will have two minutes to view the photo of the nightmare.")
        input("  Press enter to begin")
        pic.show()
        time.sleep(120)
    pic.close()
"""

def searchInv(num):
    for x in items.keys():
        if x[-2:] == num:
            return True
    return False

"""
def showImage(href):
    with Image.open(href) as pic:
        pic.show()
"""
