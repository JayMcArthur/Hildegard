import random, json


def bowsAndBreakfastLoader(deck):
    with open('cards/bows_and_breakfast/bows_and_breakfast.json') as json_file:
        file_contents = json.load(json_file)
        # Add Squirrel into hunt deck
        for card in file_contents["386"]:
            deck["192"].append(card)
    return deck


def waffledLoader(deck):
    with open('cards/bows_and_breakfast/bows_and_breakfast.json') as json_file:
        file_contents = json.load(json_file)
        # Add all Waffled Cards
        for key, card_list in file_contents.items():
            if key not in ["382", "383", "384", "385"]:
                continue
            deck[key] = card_list
        # Add Waffled interrupt to card 2
        deck["2"]["text"][len(deck["2"]["text"])-1]["effect"].append(["interrupt_pull_card", 382])
    return deck


def calledToArmsLoader(deck):
    with open('cards/bows_and_breakfast/bows_and_breakfast.json') as json_file:
        file_contents = json.load(json_file)
        # Add all Archers to Archer Deck
        for card in file_contents["380"]:
            deck["374"].append(card)
        # Return Archer Deck to 7 random cards
        while len(deck["374"]) > 7:
            deck["374"].pop(random.randrange(len(deck["374"])))

    return deck

