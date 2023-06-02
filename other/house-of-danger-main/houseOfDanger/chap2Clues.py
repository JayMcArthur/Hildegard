import chap2Cards as ch2
from functions import *

def twenty_eight(psych):
    text = [
        "'My great-great-great grandson has built some kind of laboratory beneath the house. You'll need this if you "
        "wish to get very far.' Your psychic senses tell you this is an important item.",
        "Keep this item. Move forward 1 space on the Psychic Scale.", "Finish Story Card 34."
    ]
    wrapFast(text)
    addInv('items', 'Keycard 28', 'Your psychic senses tell you this is an important item.')
    psych = psychUp(psych, 1)
    return psych


def twenty_nine(psych):
    text = [
        "You open a drawer and find a book. The middle portions of its pages are cut away, and inside the hollowed area "
        "sits a glass key. Perhaps you'll find a use for this.",
        "Keep this item. Move forward 1 space on the Psychic Scale.", "Finish Story Card 39"
    ]
    wrapFast(text)
    addInv('items', 'Glass Key 29', 'A glass key you found hidden in a book in a drawer.')
    psych = psychUp(psych, 1)
    return psych


def thirty(psych):
    text = [
        "The queen's hands don't move, but you hear her incredible piano playing swirl through the parlor, as fast as "
        "the wind. Now it's your turn. Reaching out to the piano with your mind, you weave notes into an intricate "
        "manic waltz, even faster and more beautiful than the queen's. Your music dances throughout the room. The "
        "queen's crown falls to the floor. You've bested her. You win!",
        "Keep this card. Move forward 2 spaces on the Psychic Scale.", "Finish Story Card 57."
    ]
    wrapFast(text)
    addInv('items', "The Queen's Waltz 30", 'Proof you bested the doll queen in a psychic piano duel.')
    psych = psychUp(psych, 2)
    return psych


def thirty_one():
    text = [
        "Inside the sharp-toothed jaws of a mounted cheetah head, you find a battery. It could power a flashlight. Or a "
        "Taser. Or who knows.", "Keep this card.", "Finish Story Card 42."
    ]
    wrapFast(text)
    addInv('items', 'Battery 31', 'It could power a flashlight. Or a Taser. Or who knows.')


def thirty_two(psych, danger):
    text = [
        "You offer the sabre to the advancing apparition. He pauses and takes it, sliding the sword into his scabbard. "
        "It fits perfectly.", "He looks at you and starts to speak.",
        "Move forward 2 spaces on the Psychic Scale. Lower Danger Meter by two. Go to Story Card 34."
    ]
    wrap(text)
    psych = psychUp(psych, 2)
    danger = dangerDown(danger, 2)
    psych, danger = ch2.thirty_four(psych, danger)
    return psych, danger


def thirty_three():
    text = [
        "BONUS STORY CHOICE", "You find a switch, and the pool table turns over to reveal a strange, motorized "
                              "mechanism. Maybe it lowers the table down to the basement?"
    ]
    wrap(text)


def thirty_four():
    text = [
        "BONUS STORY CHOICE",
        "The cupboards are entirely empty, but the back of one of them opens to reveal a secret passage and a stairway."
    ]
    wrap(text)


def thirty_five():
    text = [
        "Item Found! Climbing Boots: climbing roll + 2",
        "Look at these things! You'll be able to climb like a squirrel wearing these boots.", "Keep this item.",
        "Finish Story Card 56."
    ]
    wrap(text)
    addInv('climbing', 'Climbing Boots 35',
           "Look at these things! You'll be able to climb like a squirrel wearing these boots.", amount=2)


def thirty_six():
    text = [
        "'Those ghosts are born of tragedy,' he says. He hands you a newspaper clipping detailing a fire at the Hedge "
        "Brook Prison. 'All the inmates were locked inside during the blaze.' He drops his head, and his voice becomes "
        "a whisper as he says, 'None survived.'",
        "He continues: 'This house was built on the prison grounds, and its spirits have always been restless. But "
        "something has riled them up these recent weeks, and they've grown even angrier.'", "Finish Story Card 34."
    ]
    wrap(text)


def thirty_seven(psych, danger):
    text = [
        "You're in! You're exhausted, you're bleeding, and there are shards of glass all over the floor, but you've "
        "made it into the solarium. Hopefully after the racket you made, no one will come rushing to investigate.",
        "Go to Story Card 48."
    ]
    wrapFast(text)
    psych, danger = ch2.forty_eight(psych, danger)
    return psych, danger


def thirty_eight(psych):
    text = [
        "ITEM FOUND: Briefcase Full of Money",
        "You are currently holding a briefcase that contains more money than Sergeant Morrison and Detective Murphy "
        "earn in two years. Your psychic senses tell you this is an important item.",
        "Keep this item. Move forward 1 space on the Psychic Scale.", "Finish Story Card 33"
    ]
    wrap(text)
    addInv('items', 'Briefcase Full of Money 38', 'A briefcase full of money, more than most would make in two years.')
    psych = psychUp(psych, 1)
    return psych


def thirty_nine(psych, danger):
    text = [
        "ITEM FOUND: Large Metal Rod",
        "You calmly explain to the woman that you'd rather not go with her, and she returns to tending her plants. You "
        "grab the shiny object before leaving and find that it's warm to the touch. Your psychic senses tell you this "
        "is an important item. You slip away to the art gallery.",
        "Keep this item. Move forward 3 spaces on the Psychic Scale.", "Go to Story Card 32."
    ]
    wrap(text)
    psych = psychUp(psych, 3)
    addInv('items', 'Large Metal Rod 39', 'Warm to the touch, you found it in a plant in the solarium.')
    psych, danger = ch2.thirty_two(psych, danger)
    return psych, danger


def forty(psych, danger):
    text = [
        "You climb the ladder into darkness. The temperature warms as you leave the wine cellar, but as you ascend a "
        "narrow shaft for what must be several minutes, you feel the temperature grow colder again every ten rungs or "
        "so. Could you be going in circles... vertically? No, you're pretty sure the laws of physics don't work that "
        "way. Finally, the ladder ends. You open a door in front of you, and jump out into a room.",
        "Go to Story Card 36."
    ]
    wrap(text)
    psych, danger = ch2.thirty_six(psych, danger)
    return psych, danger


def forty_one(psych, danger):
    text = [
        "Seeing something reflective inside the open mouth of a cheetah head mounted on the wall, you reach your hand "
        "inside and clumsily bump its canine teeth, causing its jaws to clamp down on your hand.",
        "Overcome by searing pain, you struggle to pull it out and succeed at escaping with all your fingers-- barely.",
        "Raise Danger Meter by four.", "Finish Story Card 42."
    ]
    wrap(text)
    psych, danger = dangerUp(danger, psych, 4)
    return psych, danger


def forty_two():
    showImage('clue42.jpg')


def forty_three():
    text = [
        "The ghost's eyes look grim. 'I would turn back if I were you. THe source of those nightmares is something "
        "truly frightening, indeed. You don't want to tamper with forces that are far beyond you. You won't fare well.'",
        "Finish Story Card 34."
    ]
    wrapFast(text)


def forty_four(psych, danger):
    text = [
        "You stack several crates to build a makeshift staircase and climb into the hole in the ceiling. YOu find "
        "yourself inside a disorienting maze of air ducts. Eventually, reach an exterior vent.",
        "Opening the vent, you get a face full of wind and rain. You then expertly climb down a vine-covered lattice "
        "onto a rain-drenched path.", "Go to Story Card 46."
    ]
    wrap(text)
    psych, danger = ch2.forty_six(psych, danger)
    return psych, danger


def forty_five(psych, danger):
    text = [
        "You race down the hallway past photographs and paintings of an old prison. You reach the end of the hall and "
        "find a metal door.", "Go to Story Card 60"
    ]
    wrapFast(text)
    psych, danger = ch2.sixty(psych, danger)
    return psych, danger


def forty_six(psych, danger):
    text = [
        "You put the glass key in the lock, hold your breath, and twist your wrist very slowly. The lock seems sturdy "
        "enough, but the key looks like it would shatter if you dropped it.",
        "With a sharp CLINK, the door pops open in a very swift and satisfying motion. You're in!", "Go to Story Card 48"
    ]
    wrap(text)
    psych, danger = ch2.forty_eight(psych, danger)
    return psych, danger


def forty_seven(psych, danger):
    text = [
        "You'll have to use all your might to throw the ring through the portal before jumping through to the other "
        "side, where you sense the portal's magic will surely return you to normal size.", "REQUIRED STRENGTH CHALLENGE",
        "Throw the ring through the portal", "WIN: Lower Danger Meter by two and draw CLUE 55.",
        "LOSE: Raise Danger Meter by one and try again."
    ]
    wrapFast(text)
    chal, danger = challenge('required', 'strength', danger)
    while chal == 'fail':
        wrapFast('You missed!')
        psych, danger = dangerUp(danger, psych, 1)
        wrapFast('Trying again...')
        chal, danger = challenge('required', 'strength', danger)
    if chal == 'win':
        danger = dangerDown(danger, 2)
        psych, danger = fifty_five(psych, danger)
    return psych, danger


def forty_eight():
    text = [
        "You creep closer and overhear bits and pieces of conversation.",
        "One ghost mentions barely surviving a savage attack and locking 'the dangerous one' in the secret passage "
        "between the kitchen and the master bedroom.", "Finish Story Card 51."
    ]
    wrap(text)


def forty_nine():
    text = [
        "ITEM FOUND: Sandwich",
        "You find a delicious-looking sandwich in the fridge. Discard at any time to lower Danger Meter by four.",
        "Keep this item", "Finish Story Card 54."
    ]
    wrapFast(text)
    addInv('danger', 'Sandwich', 'Discard at any time to lower Danger Meter by four.', amount=4)


def fifty(psych):
    text = [
        "You sneeze, awaking the mouse, which scurries away. In the bed, you see it was sleeping on top of the Marsden "
        "family ring!",
        "In your tiny state, it's as big as a truck tire. You must roll it to move it. Your psychic senses tell you "
        "this is an important item.", "Keep this item. Move forward 1 space on the Psychic Scale.",
        "Finish Story Card 41."
    ]
    wrap(text)
    addInv('items', 'Marsden Family Ring 50', 'Found underneath a sleeping toy mouse in the dollhouse.')
    psych = psychUp(psych, 1)
    return psych


def fifty_one(psych, danger):
    text = [
        "You swing your fists at the spirit, and you're surprised to find that your blows actually land. You're really "
        "punching a ghost! The fight is long and difficult, and by the end of it the room's in pretty bad shape. "
        "However, the ghost seems impressed with you.",
        "'That's the best fight I've had in ages,' he says. 'I guess you deserve some answers, then.'",
        "Lower Danger Meter by four and go to Story Card 34."
    ]
    wrap(text)
    danger = dangerDown(danger, 4)
    psych, danger = ch2.thirty_four(psych, danger)
    return psych, danger


def fifty_two():
    showImage('clue52.jpg')


def fifty_three(psych, danger):
    text = [
        "The woman doesn't care what you say. She doesn't bother responding, but her lips curl into a cruel smile.",
        "Go to Story Card 55."
    ]
    wrapFast(text)
    psych, danger = ch2.fifty_five(psych, danger)
    return psych, danger


def fifty_four():
    showImage('clue54.jpg')


def fifty_five(psych, danger):
    text = [
        "You take a deep breath and jump into the portal. A pins-and-needles sensation spreads over your body as you "
        "travel the dimensional pathway. When you reach the other side, you're standing in the solarium you saw in the "
        "picture. You've returned to your normal size.", "Go to Story Card 48"
    ]
    wrapFast(text)
    psych, danger = ch2.forty_eight(psych, danger)
    return psych, danger


def fifty_six(psych):
    text = [
        "You project your thoughts at the little king, like light through a magnifying glass. You focus on the doll's "
        "mind, narrowing your thoughts into a tight beam.",
        "Finally, when you can hardly take any more... the doll blinks. You won!",
        "Keep this card. Move forward 2 spaces on the Psychic Scale.", "Finish Story Card 35."
    ]
    wrap(text)
    psych = psychUp(psych, 2)
    return psych


def fifty_seven():
    text = [
        "Chapter Two Goal:", "Find access to the basement."
    ]
    wrap(text)
