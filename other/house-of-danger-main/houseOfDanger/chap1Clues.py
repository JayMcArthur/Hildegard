import chap1Cards as ch1
from functions import *

def one(psych, danger):
    text = [
        "You turn and follow a path for several minutes. Wait... this looks familiar...",
        "Raise Danger Meter by one and draw CLUE 11."
    ]
    wrap(text)
    psych, danger = dangerUp(danger, psych, 1)
    psych, danger = eleven(psych, danger)
    return psych, danger


def two(psych):
    text = [
        "Obtained Item: Calvary Sabre, Fighting roll + 2", "The sabre comes loose in your hand. It's heavy and quite "
                                                           "sharp. Your psychic senses tell you this is an important item.",
        "Keep this item. Move forward 2 spaces on the Psychic Scale. Finish Story Card 4"
    ]
    wrap(text)
    addInv('fighting', 'Cavalry Sabre 2', "It's very heavy and quite sharp. Your psychic senses tell you this is an "
                                          "important item.", amount=2)
    psych = psychUp(psych, 2)
    return psych


def three(psych):
    text = [
        "ITEM FOUND: Truck Key", "Not only is the lockbox open, but inside you find a key to a truck. Your Psychic "
                                 "senses tell you this is an important item.",
        "Keep this item. Move forward 2 spaces on the Psychic Scale. Finish Story Card 18."
    ]
    wrap(text)
    addInv('items', 'Truck Key 3',
           'A truck key you found in a lockbox. Your psychic senses tell you this is an important '
           'item.')
    psych = psychUp(psych, 2)
    return psych


def four():
    text = [
        "ITEM FOUND: Battery", "You found a battery in a drawer. It could power a flashlight. Or a Taser. Or who knows "
                               "what else.", "Keep this item. Finish Story Card 19."
    ]
    addInv('items', 'Battery 4',
           'You found a battery in a drawer. It could power a flashlight. Or a Taser. Or who knows '
           'what else.')
    wrap(text)


def five():
    text = [
        "ITEM FOUND: Shears, Strength roll + 2",
        "You pull a pair of garden shears from the shrub. They could help you pry something open.",
        "Keep this item. Finish Story card 15."
    ]
    wrap(text)
    addInv('strength', 'Shears 5',
           'A pair of garden shears you pulled from a shrub. They could help you pry something '
           'open.', amount=2)


def six():
    text = [
        "ITEM FOUND: First Aid Kit", "The first aid kit is fully stocked. The way things are going, you're sure you'll"
                                     "need it. Discard at any time to lower Danger Meter by four.",
        "Keep this item. Finish Story Card 27."
    ]
    wrap(text)
    addInv('danger', 'First Aid Kit 6',
           "This first aid kit is fully stocked. The way things are going, you're sure you'll need it. Discard at any "
           "time to lower Danger Meter by four.", amount=4)


def seven(psychic, danger):
    text = [
        "ITEM FOUND: Satellite Dish", "Your psychic senses tell you this is an important item. You look to your left "
                                      "and see a path to a driveway that might be the front of the house. You jump off "
                                      "the gazebo and run to check it out.",
        "Keep this item. Move forward 1 space on the Psychic Scale. Go to Story Card 30."
    ]
    wrap(text)
    addInv('items', 'Satellite Dish 7', 'Your psychic senses tell you this is an important item.')
    psychic = psychUp(psychic, 1)
    psych, danger = ch1.thirty(psychic, danger)
    return psych, danger


def eight(psych):
    text = [
        "You walk down the steps into the water and see what's making the waves: a strange, whirring metal sphere, "
        "slightly bigger than a softball. You impulsively grab it.",
        "The sphere vibrates in your hand. There are two buttons on it. You press one. Nothing happens. You press the "
        "other button. The sphere continues to vibrate. Instinctively, you press both buttons at the same time. The "
        "sphere stops moving and begins to glow.", "Draw CLUE 21."
    ]
    wrap(text)
    psych = twenty_one(psych)
    return psych


def nine(psych, danger):
    text = [
        "You turn and follow a path deeper into the maze. You feel like you're going in the right direction.",
        "To go left, enter 'eleven' to draw CLUE 11.", "To go right, enter 'twelve' to draw CLUE 12."
    ]
    wrap(text)
    options = ('eleven', 'twelve', '11', '12')
    choice = choose(options)
    if choice in ['11', 'eleven']:
        psych, danger = eleven(psych, danger)
    else:
        psych, danger = twelve(psych, danger)
    return psych, danger


def ten(psych, danger):
    text = [
        "It's probably unwise to engage such a savage beast in combat, but Danger is your middle name. You land a few "
        "quick jabs on the creature before it can react, and then you throw it to the ground. You stand there for a "
        "moment, your confidence high. Then, the creature leaps to its feet and rushes you. You managed to win Round "
        "One, but you're in no hurry to start Round Two, so you race for the shadows beside a big boulder before the "
        "creature can get its hands on you.", "Draw CLUE 25."
    ]
    wrap(text)
    psych, danger = twenty_five(psych, danger)
    return psych, danger


def eleven(psych, danger):
    text = [
        "You keep going. And going. It seems like you've just walked in a circle!", "Raise Danger Meter by two and draw"
                                                                                    "CLUE 12."
    ]
    wrap(text)
    psych, danger = dangerUp(danger, psych, 2)
    psych, danger = twelve(psych, danger)
    return psych, danger


def twelve(psych, danger):
    text = [
        "You feel like you might be getting close to the end of the maze!", "To go left, enter 'thirteen' to draw CLUE"
                                                                            " 13",
        "To go right, enter 'fourteen' to draw CLUE 14."
    ]
    wrap(text)
    options = ('thirteen', 'fourteen', '13', '14')
    choice = choose(options)
    if choice in ['thirteen', '13']:
        psych, danger = thirteen(psych, danger)
    else:
        psych, danger = fourteen(psych, danger)
    return psych, danger


def thirteen(psych, danger):
    text = [
        "Finally you see it... The end of the maze!", "Go to Story Card 18"
    ]
    wrap(text)
    psych, danger = ch1.eighteen(psych, danger)
    return psych, danger


def fourteen(psych, danger):
    text = [
        "You'd think you'd be better at this by now...", "Raise Danger Meter by two and draw CLUE 13"
    ]
    wrap(text)
    psych, danger = dangerUp(danger, psych, 2)
    psych, danger = thirteen(psych, danger)
    return psych, danger


def fifteen():
    text = [
        "ITEM FOUND: Flashlight",
        "The cigar box contains a flashlight. You check and discover that it has no batteries.",
        "Discard any Battery to automatically win a Perception challenge.", "Keep this item. Finish Story Card 14"
    ]
    wrap(text)
    addInv('danger', 'Flashlight 15', 'Discard any Battery to automatically win a Perception challenge')


def sixteen():
    text = [
        "It takes some muscle, but you manage to remove the lid and are surprised to find that not only is there no "
        "body, but an opening to a secret passageway offers yet another way out of the mausoleum.",
        "To take the secret passageway, enter 'twenty four' to draw CLUE 24."
    ]
    wrap(text)


def seventeen(psych, danger):
    text = [
        "Your fingertips graze a piece of the satellite dish, but you can't quite grab it. You reach too far, lose your"
        " balance, and tumble from the gazebo and down a short hill.",
        "Your confusion from the fall slowly subsides, and you hear the sound of a beautiful violin nearby. You stumble"
        " off in the direction of the music.", "Raise Danger Meter by two. Go to Story Card 17."
    ]
    wrap(text)
    psych, danger = dangerUp(danger, psych, 2)
    psych, danger = ch1.seventeen(psych, danger)
    return psych, danger


def eighteen():
    text = [
        "When you inadvertently hit a hidden switch, the statue slides to one side, revealing a cement passage."
    ]
    wrap(text)


def nineteen(psych):
    text = [
        "The paper looks like a map to the hedge maze. Your psychic senses tell you this is an important item.",
        "Keep this item. Move forward 1 space on the Psychic Scale. Finish Story Card 26."
    ]
    wrap(text)
    psych = psychUp(psych, 1)
    addInv('items', 'Hedge Maze Map 19',
           'The paper looks like a map to the hedge maze. Your psychic senses tell you this '
           'is an important item.')
    return psych


def twenty(psych, danger):
    text = [
        "The thing -- whatever it is -- wraps more tightly around your leg. It's pulling you down! Another tendril (or "
        "tentacle?) slides around your neck. You pry it off, and with the last of your strength , you give a powerful "
        "kick, and you're free. Just like that, the thing is gone. You emerge into a swimming pool with a lush pool "
        "house next to it.", "Lower Danger Meter by two and go to Story Card 23."
    ]
    wrap(text)
    danger = dangerDown(danger, 2)
    psych, danger = ch1.twenty_three(psych, danger)
    return psych, danger


def twenty_one(psych):
    text = [
        "ITEM FOUND: Whirring Metal Sphere", "Your psychic senses tell you this is an important item.",
        "Keep this item."
    ]
    wrap(text)
    addInv('items', 'Whirring Metal Sphere 21', 'Your psychic senses tell you this is an important item.')
    psych = psychUp(psych, 3)
    return psych


def twenty_two(psych, danger):
    text = [
        "You hold on to the top of the gazebo with one hand and time your lunge perfectly -- you snag a chunk of the "
        "whirling satellite dish.", "The piece appears to be made by hand. An engraving on it reads PLANET OF CRYSTALS."
    ]
    wrap(text)
    psych, danger = seven(psych, danger)
    return psych, danger


def twenty_three(psych):
    text = [
        "ITEM FOUND: Large Wooden Dowel", "You find a large wooden dowel. Your psychic senses tell you this is an "
                                          "important item.",
        "Keep this item. Move forward 1 space on the Psychic Scale. Finish Story Card 5"
    ]
    wrap(text)
    addInv('strength', 'Large Wooden Dowel 23',
           'Your psychic senses tell you this is an important item. Fighting roll + 2',
           2)
    psych = psychUp(psych, 1)
    return psych


def twenty_four(psych, danger):
    text = [
        "You travel through the tunnel for what feels like forever. The light disappears, and the tunnel "
        "eventually ends. You feel frightened and trapped. You want to run back and try the other routes of the mausoleum.",
        "Before you go, you feel around in the dark. There's nothing in front of you or to your sides. But you discover "
        "a mossy hatch in the tunnel ceiling. You turn the handle, and the hatch opens on to a grassy patch at the entrance "
        "to a hedge maze.", "Go to Story Card 12"
    ]
    wrap(text)
    psych, danger = ch1.twelve(psych, danger)
    return psych, danger


def twenty_five(psych, danger):
    text = [
        "ITEM FOUND: High-Powered Binoculars, Perception roll + 2",
        "You find a pair of binoculars in the shadows. With the creature on the loose, you can't hide here forever, so "
        "you run to the guardhouse.", "Keep this item. Go to Story card 19."
    ]
    wrap(text)
    addInv('perception', 'High-Powered Binoculars 25', 'Perception Roll + 2', 2)
    psych, danger = ch1.nineteen(psych, danger)
    return psych, danger


def twenty_six():
    text = [
        "CHAPTER ONE GOAL", "Get inside the Marsden House"
    ]
    wrap(text)


def twenty_seven():
#    clue27 = Image.open('clue27.jpg')
#    clue27.show()
#    addInv('items', 'Premonition 27', 'clue27.jpg')
     pass   
