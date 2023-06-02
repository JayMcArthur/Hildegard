import json


def greatOutdoorsLoader(deck):
    with open('cards/great_outdoors/great_outdoors.json') as json_file:
        file_contents = json.load(json_file)
        for key, card_list in file_contents.items():
            deck[key] = card_list
    return deck
