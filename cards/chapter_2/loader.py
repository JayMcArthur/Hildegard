import json


def chapter2loader(deck):
    with open('cards/chapter_2/chapter_2.json') as json_file:
        file_contents = json.load(json_file)
        for key, card_list in file_contents.items():
            deck[key] = card_list
    return deck


