import json


def oaksCrossingLoader(deck):
    with open('cards/oaks_crossing/oaks_crossing.json') as json_file:
        file_contents = json.load(json_file)
        for key, card_list in file_contents.items():
            deck[key] = card_list
    return deck

