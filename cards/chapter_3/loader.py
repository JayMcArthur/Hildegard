import json


def chapter3loader(deck):
    with open('cards/chapter_3/chapter_3.json') as json_file:
        file_contents = json.load(json_file)
        for key, card_list in file_contents.items():
            deck[key] = card_list
    return deck
