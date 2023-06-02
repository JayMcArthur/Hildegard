import json


def crowsAndCrawdadsLoader(deck):
    with open('cards/crows_and_crawdads/crows_and_crawdads.json') as json_file:
        file_contents = json.load(json_file)
        for key, card_list in file_contents.items():
            deck[key] = card_list
    return deck

