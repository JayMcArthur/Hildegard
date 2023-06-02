import chap1Cards as ch1
import chap2Cards as ch2
from functions import save
from functions import loadSave


print('Welcome To Choose Your Own Adventure: House of Danger, a cooperative adventure game by Prospero Hall, '
      'coded by Evelyn Kammerzell.')
start = input('Would you like to load a save file? [y/n] ')
while start not in ['y', 'n']:
    start = input("Please enter 'y' or 'n': ")
if start == 'n':
    psych = 3
    danger = 0

    psych, danger = ch1.one(psych, danger)
    choice = input('Would you like to save your progress? [y/n] ')
    while choice not in ['y', 'n']:
        choice = input("Please enter 'y' or 'n': ")
    if choice == 'y':
        save(psych, danger, 1)


if start == 'y':
    psych, danger, chapter = loadSave()
    if chapter == 1:
        psych, danger = ch2.thirty_one(psych, danger)
        chapter = 2
        choice = input('Would you like to save your progress? [y/n] ')
        while choice not in ['y', 'n']:
            choice = input("Please enter 'y' or 'n': ")
        if choice == 'y':
            save(psych, danger, chapter)
    if chapter == 2:
        #psych, danger = ch3.one(psych, danger)
        chapter = 3
        choice = input('Would you like to save your progress? [y/n] ')
        while choice not in ['y', 'n']:
            choice = input("Please enter 'y' or 'n': ")
        if choice == 'y':
            save(psych, danger, chapter)
    if chapter == 3:
        #psych, danger = ch4.one(psych, danger)
        chapter = 4
        choice = input('Would you like to save your progress? [y/n] ')
        while choice not in ['y', 'n']:
            choice = input("Please enter 'y' or 'n': ")
        if choice == 'y':
            save(psych, danger, chapter)
    if chapter == 4:
        #psych, danger = ch5.one(psych, danger)
        pass

