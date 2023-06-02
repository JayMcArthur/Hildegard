import chap2Clues as clue2
from functions import *


def thirty_one(psych, danger):
    text = [
        "Chapter Two: The Mansion",
        "You made it! You're inside the Marsden house, the cursed edifice that has been haunting your nightmares for "
        "weeks. Your trek through the mansion's grounds has left you with far more questions than answers, to the point"
        " where you have to wonder if the smart move would be to turn around right now and forget you ever came to this"
        " infernal place.",
        "You're no quitter though. You're an aspiring detective and psychic investigator. You won't give up this case "
        "until you find out why a spooky, futuristic mansion you'd never seen before has somehow found its way into "
        "your dreams. And why you got a call from the house this morning.",
        "You're standing in a grand foyer. Its modern decor is elegant in its minimalism. Suddenly, a man in a delivery"
        " uniform bursts through a set of tall, double doors, screaming.",
        "'Help! Help! They're after me!' the man cries. He rushes toward you, but suddenly drops to the ground as if he"
        " had been hit by an invisible hammer. You dash to his side and hear his breath coming in short gasps that "
        "sound almost like sobs. He gives a terrible shriek and lies still. 'This man has been frightened to death,' "
        "you think.",
        "Just then he inhales sharply, jumps to his feet, and bolts past you and out of the house. You breathe a deep "
        "sigh of relief. So, not quite to death. Something falls from his clothing as he makes his exit, and it hits "
        "the floor, tinkling. You kneel down to inspect the object and discover it's a small dart, the kind that might "
        "have come from a blow gun. Whatever this man was afraid of, his fear seems to have been justified.",
        "Just how dangerous is this house? As your thoughts swirl, a loud, buzzing noise erupts from somewhere beneath "
        "your feet, shaking the floor. The noise is so loud it drowns out the gathering storm outside.",
        "Just as quickly as it came, the noise stops. It sure sounds like something weird is happening beneath the "
        "manor. You're willing to bet that -- whatever is happening in this place -- the answers await you down there."
    ]
    wrap(text)
    clue2.fifty_seven()
    text = [
        "You don't see any way to a lower level from the foyer. Rather, a sweeping stairway leads upstairs, while the "
        "double doors that the frightened man ran through head off to your right, and a smaller door, slightly ajar, "
        "leads in the opposite direction.", "If you take the stairs to the second floor, enter 'thirty nine' to go to "
        "Story Card 39.", "If you go through the double doors, enter 'fifty one' to go to Story Card 51.",
        "If you walk through the smaller door, enter 'forty two' to go to Story Card 42."
    ]
    wrapFast(text)
    options = ['thirty nine', '39', 'fifty one', '51', 'forty two', '42']
    choice = choose(options)
    if choice in ['thirty nine', '39']:
        psych, danger = thirty_nine(psych, danger)
    elif choice in ['fifty one', '51']:
        psych, danger = fifty_one(psych, danger)
    else:
        psych, danger = forty_two(psych, danger)
    return psych, danger


def thirty_two(psych, danger):
    text = [
        "Stepping into the marble-floored art gallery, you are amazed by more than a hundred gold-framed paintings, "
        "plus countless abstract, modern sculptures on pedestals. Wow! The entire collection must be worth gazillions. "
        "Too bad you've got no time to admire any of it. You're eager to keep moving.",
        "French doors lead to the study, and a doorway leads outside. You can see a pathway leading to an attached "
        "structure that appears to be a mother-in-law apartment."
    ]
    wrap(text)
    text = [
        "PREMONITION", "If you are Level 2 or higher on the Psychic Scale, draw CLUE 54."
    ]
    wrapFast(text)
    if psych >= 6:
        print('You are Level 2 or higher!')
        clue2.fifty_four()
    else:
        print('You are not high enough level for this premonition.')
    text = [
        "If you walk through the French doors to the study, enter 'thirty three' to go to Story Card 33.",
        "If you  take the path outside to the mother-in-law apartment, enter 'forty six' to go to Story Card 46."
    ]
    wrapFast(text)
    options = ('thirty three', '33', 'forty six', '46')
    choice = choose(options)
    if choice in ['thirty three', '33']:
        psych, danger = thirty_three(psych, danger)
    else:
        psych, danger = forty_six(psych, danger)
    return psych, danger


def thirty_three(psych, danger):
    text = [
        "Once inside the study, you are shocked to find twelve pairs of eyes staring at you in outrage. You stop dead "
        "in your tracks. There are a dozen shady-looking people, all stuffing briefcases with bundles of cold, hard "
        "cash. Literally, they're taking money out of ice-filled coolers.",
        "You take another step, and all but one of the guys take off, suddenly spooked. The last one turns and glares "
        "at you. Since he's holding his briefcase tightly with both hands, you're pretty sure you can take him.",
        "You see a hallway on the other side of the room that might serve to be a quick exit."
    ]
    wrap(text)
    text = [
        "Optional Fighting Challenge", "Wrestle the man with the cash-filled briefcase", "WIN: Draw CLUE 38",
        "LOSE: Ranger Danger Meter by three. You may try again."
    ]
    wrapFast(text)
    chal, danger = challenge('optional', 'fighting', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print('You were beaten by the man with the briefcase!')
        psych, danger = dangerUp(danger, psych, 3)
        choice = input('Would you like to try wrestling him again? [y/n] ')
        while choice not in ['y', 'n']:
            choice = input('Please enter y or n: ')
        while choice == 'y':
            chal, danger = challenge('optional', 'fighting', danger)
            if chal == 'quit':
                choice = ''
            elif chal == 'fail':
                print('You were beaten by the man with the briefcase!')
                psych, danger = dangerUp(danger, psych, 3)
                choice = input('Would you like to try wrestling him again? [y/n] ')
                while choice not in ['y', 'n']:
                    choice = input('Please enter y or n: ')
            else:
                choice = ''
    elif chal == 'win':
        psych = clue2.thirty_eight(psych)
    print('  Head down the hallway by drawing CLUE 45')
    psych, danger = clue2.forty_five(psych, danger)
    return psych, danger


def thirty_four(psych, danger):
    text = [
        "I am General Henry Marsden of the Union Army, and this estate has passed through my family for generations, "
        "ever since the first settlers built this town. I regret that I cannot stay long, for though our meeting has "
        "invigorated me, I must soon return to my penance... below. Before I go, however, I will answer any one inquiry"
        " you might have.", "Choose One:"
    ]
    wrap(text)
    text = [
        "If you ask the ghost about the noises in the basement, enter 'twenty eight' for CLUE 28.",
        "If you ask the ghost about other ghosts in the mansion, enter 'thirty six' for CLUE 36.",
        "If you ask the ghost about your nightmares, enter 'forty three' for CLUE 43."
    ]
    wrapFast(text)
    options = ('twenty eight', '28', 'thirty six', '36', 'forty three', '43')
    choice = choose(options)
    if choice in ['twenty eight', '28']:
        psych = clue2.twenty_eight(psych)
    elif choice in ['thirty six', '36']:
        clue2.thirty_six()
    else:
        clue2.forty_three()
    wrapFast(["If you return to the hallway, enter 'forty' to go to Story Card 40.", "If you check out the bathroom, "
              "enter 'fifty' to go to Story Card 50."])
    options = ('forty', '40', 'fifty', '50')
    choice = choose(options)
    if choice in ['forty', '40']:
        psych, danger = forty(psych, danger)
    else:
        psych, danger = fifty(psych, danger)
    return psych, danger


def thirty_five(psych, danger):
    text = [
        "Seated at the head of the dollhouse dining room table is a doll wearing a crown. It's a doll king with oddly "
        "compelling glass eyes. They sparkle with a kind of dark power. As you look into those eyes, you sense a "
        "strange tingle in your mind. This doll is reaching out to you mentally. You don't know why, but you feel that "
        "he wants to fight you... on the plane of pure thought. You sense this could help you strengthen your psychic "
        "abilities.", "Around the dining room table, two doors lead to other rooms inside the dollhouse."
    ]
    wrap(text)
    text = [
        "OPTIONAL PERCEPTION CHALLENGE", "Overpower the doll king with your mind", "WIN: Draw CLUE 56.",
        "LOSE: Raise Danger Meter by three. You may try again."
    ]
    wrapFast(text)
    chal, danger = challenge('optional', 'perception', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print('You were beaten by the doll king!')
        psych, danger = dangerUp(danger, psych, 3)
        choice = input('Would you like to try overpowering him again? [y/n] ')
        while choice not in ['y', 'n']:
            choice = input('Please enter y or n: ')
        while choice == 'y':
            chal, danger = challenge('optional', 'fighting', danger)
            if chal == 'quit':
                choice = ''
            elif chal == 'fail':
                print('You were beaten by the doll king!')
                psych, danger = dangerUp(danger, psych, 3)
                choice = input('Would you like to try overpowering him again? [y/n] ')
                while choice not in ['y', 'n']:
                    choice = input('Please enter y or n: ')
            else:
                choice = ''
    elif chal == 'win':
        psych = clue2.fifty_six(psych)
    text = [
        "If you go to the dollhouse parlor, enter 'fifty seven' to go to Story Card 57.",
        "If you go to the dollhouse bedroom, enter 'forty one' to go to Story Card 41."
    ]
    wrapFast(text)
    options = ('fifty seven', '57', 'forty one', '41')
    choice = choose(options)
    if choice in ['fifty seven', '57']:
        psych, danger = fifty_seven(psych, danger)
    else:
        psych, danger = forty_one(psych, danger)
    return psych, danger


def thirty_six(psych, danger):
    text = [
        "You arrive in a large room with high ceilings and five billiard tables lined up in the center. Four of the "
        "tables are lit by exquisite lamps suspended above them. Billiard balls are neatly racked on the fifth table, "
        "which sits in the shadows, as if waiting for a game to begin.",
        "A small bar stands against one wall. Atop the bar, fifteen overturned crystal glasses are arranged to form a "
        "pyramid.", "There's a weirdly small door on the far side of the room. It seems to have been designed for a "
        "child, but you might be able to squeeze through it if you tried. You hear rain pattering against a skylight "
                    "window -- it's nearly dark outside, and the rain appears to have started in earnest."
    ]
    wrap(text)
    text = [
        "PREMONITION", "If you are Level 2 or higher on the Psychic Scale, draw CLUE 52"
    ]
    wrapFast(text)
    if psych >= 6:
        print('You received the premonition!')
        clue2.fifty_two()
    else:
        print('You were not able to receive the premonition.')
    text = [
        "OPTIONAL PERCEPTION CHALLENGE", "Inspect the billiards table in the shadows", "WIN: Draw CLUE 33",
        "LOSE: Raise Danger Meter by one"
    ]
    wrapFast(text)
    check = False
    chal, danger = challenge('optional', 'perception', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print("You failed to find anything around the billiards table.")
        psych, danger = dangerUp(danger, psych, 1)
    else:
        clue2.thirty_three()
        check = True
    if not check:
        print("  Squeeze through the small door by going to Story Card 44.")
        psych, danger = forty_four(psych, danger)
    else:
        text = [
            "If you want to squeeze through the small door, enter 'forty four' to go to Story Card 44.",
            "OR... If you want to hop on the table and flip the switch, enter 'fifty two' to go to Story Card 52."
        ]
        wrapFast(text)
        options = ('forty four', '44', 'fifty two', '52')
        choice = choose(options)
        if choice in ['forty four', '44']:
            psych, danger = forty_four(psych, danger)
        else:
            psych, danger = fifty_two(psych, danger)
    return psych, danger


def thirty_seven(psych, danger):
    text = [
        "You open the rattling door to reveal an impossibly long passage, slightly lit with small beams of blue light. "
        "A chill runs through your veins as an apparition materializes in the distance. The ghost wears a tattered robe,"
        " and his skin appears badly burned. One of his eyes is missing, while the other darts around nervously. He "
        "walks straight towards you, brandishing a sword in one hand.",
        "You try to run, but your legs refuse to cooperate. You're frozen in place! The spirit continues to approach "
        "you. He advances calmly, slowly moving closer and closer until he's finally upon you. You feel intense pain...",
        "And then... nothing.", "THE END", "Move back 1 space on the Psychic Scale and return to Story Card 51."
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    psych, danger = fifty_one(psych, danger)
    return psych, danger


def thirty_eight(psych, danger):
    text = [
        "Who hides a bomb in a bomb shelter? Was this thing built to protect people from a bomb, or protect a bomb from "
        "people?", "These are the thoughts you have as you are blown into a billion little pieces.", "THE END",
        "Move back 1 space on the Psychic Scale and return to Story Card 47"
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    psych, danger = forty_seven(psych, danger)
    return psych, danger


def thirty_nine(psych, danger):
    text = [
        "The stairway leads up to a long hallway. A violet rug with tasseled edges runs the length of the walls. A vase"
        " of lilies sits on an ornate side table halfway down the hall, a gorgeous wooden piece with rich floral "
        "engravings on the front and sides.",
        "Without warning, a ghostly figure comes through a door up ahead on your right. The ghost doesn't acknowledge "
        "your presence as he rushes right through a closed door on the other side of the hall.",
        "The hallway seems colder than when you entered. Should you follow the ghostly figure? Or perhaps inspect the "
        "room he came from?"
    ]
    wrap(text)
    text = [
        "OPTIONAL PERCEPTION CHALLENGE", "Search the ornate table", "(If you are Level 2 or higher on the Psychic "
        "Scale, lower your Danger Meter by 3 spots (1 level) for this challenge only.)", "WIN: Draw CLUE 29",
        "LOSE: Raise the Danger Meter by one"
    ]
    wrapFast(text)
    print(f'  You are {psychLevel(psych)} on the Psychic Scale.')
    if psych >= 6:
        boost = 3
        print('You received a Roll Boost for this Challenge!')
    else:
        boost = 0
        print('You did not receive a Roll Boost for this Challenge.')
    chal, danger = challenge('optional', 'perception', danger - boost)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print('You did not find anything in the ornate table.')
        psych, danger = dangerUp(danger, psych, 1)
    else:
        print('You found something!')
        psych = clue2.twenty_nine(psych)
    text = [
        "If you follow the ghost, enter 'fifty nine' to go to Story Card 59",
        "If you try to see where the ghost came from, enter 'thirty six' to go to Story Card 36"
    ]
    wrapFast(text)
    options = ('fifty nine', '59', 'thirty six', '36')
    choice = choose(options)
    if choice in ['fifty nine', '59']:
        psych, danger = fifty_nine(psych, danger)
    else:
        psych, danger = thirty_six(psych, danger)
    return psych, danger


def forty(psych, danger):
    text = [
        "You step backward into the hallway but find yourself somehow surrounded by a field of stars. Where did the "
        "walls go? Where is the carpet? Now there's only an endless expanse of nothingness. The stars begin to swirl "
        "around you, and you turn to find that the door you came through is gone as well.",
        "In a flash, all the stars zoom in close to your face, and you reflexively throw your arms up in front of you "
        "to avoid being struck. When you open your eyes again, you're standing on grass, and you can feel an intense "
        "heat at your back.",
        "Behind you, a huge stone structure is ablaze. Fire and smoke escape from every window, and the agonized "
        "screams of men echo through the air. A sign -- also in flames but still eligible -- reads HEDGE BROOK PRISON. "
        "You back away from the inferno, shielding your eyes... and find yourself back in the void.",
        "Now, two mysterious entrances float before you. One appears to lead into a child's playroom, and the other "
        "leads into a long, empty hallway."
    ]
    wrap(text)
    text = [
        "If you take the mysterious entrance to the playroom, enter 'forty four' to go to Story Card 44.",
        "If you take the mysterious entrance to the hallway, enter 'fifty eight' to go to Story Card 58."
    ]
    wrapFast(text)
    options = ('forty four', '44', 'fifty eight', '58')
    choice = choose(options)
    if choice in ['forty four', '44']:
        psych, danger = forty_four(psych, danger)
    else:
        psych, danger = fifty_eight(psych, danger)
    return psych, danger


def forty_one(psych, danger):
    text = [
        "The dollhouse bedroom is filled with miniature furnishings, which are now full-sized to you: a cozy chair, a "
        "dresser, a lamp, and a bed.",
        "Lying in the bed, its head on a pillow, is a stuffed mouse. It's so lifelike, you catch yourself thinking you "
        "should step quietly so you don't wake it up.",
        "Your psychic senses start to pulse. You get the feeling something very important is hidden in this room.",
        "FREE ACTION", "If you are at Level 3 or higher on the Psychic Scale, draw CLUE 50."
    ]
    wrap(text)
    print(f'  You are at {psychLevel(psych)} on the Psychic Scale.')
    if psych >= 11:
        psych = clue2.fifty(psych)
    else:
        print('You are not high enough on the Psychic Scale for this action.')
    text = [
        "If you go to the dollhouse dining room, enter 'thirty five' to go to Story Card 35",
        "If you go to the dollhouse parlor, enter 'fifty seven' to go to Story Card 57"
    ]
    wrapFast(text)
    options = ('thirty five', '35', 'fifty seven', '57')
    choice = choose(options)
    if choice in ['thirty five', '35']:
        psych, danger = thirty_five(psych, danger)
    else:
        psych, danger = fifty_seven(psych, danger)
    return psych, danger


def forty_two(psych, danger):
    text = [
        "You enter a parlor, which is decorated in a more old-fashioned way that what you've seen of the house so far: "
        "rich cherry-wood paneling covers the walls, and dozens of exotic animal heads are mounted there. Some Marsden "
        "ancestor was quite fond of hunting or, at the very least, taxidermy. Each of the trophies features the same "
        "expression: fangs bared and savage eyes that make the animal look ready to leap from the wall and pounce on "
        "you. The effect is quite unsettling. But you also sense that they might be hiding something.",
        "There are two ways out of here: an open passage that leads to an adjacent library brimming with books, and a "
        "tightly spiraled iron staircase going up."
    ]
    wrap(text)
    text = [
        "OPTIONAL PERCEPTION CHALLENGE", "Search the animal heads", "WIN: Draw CLUE 31", "LOSE: Draw CLUE 41"
    ]
    wrapFast(text)
    chal, danger = challenge('optional', 'perception', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        psych, danger = clue2.forty_one(psych, danger)
    else:
        clue2.thirty_one()
    text = [
        "If you head to the library, enter 'forty five' to go to Story Card 45",
        "If you climb the staircase, enter 'thirty six' to go to Story Card 36"
    ]
    wrapFast(text)
    options = ('forty five', '45', 'thirty six', '36')
    choice = choose(options)
    if choice in ['forty five', '45']:
        psych, danger = forty_five(psych, danger)
    else:
        psych, danger = thirty_six(psych, danger)
    return psych, danger


def forty_three(psych, danger):
    text = [
        "After ascending the ladder, you're on the roof. It's completely drenched from the rain, which of course means "
        "that you're completely drenched from the rain. But one thing up here looks complete dry: the apparition of the "
        "Union general who is standing right in front of you.",
        "'TRAITOR!' he shouts as he grows twenty feet tall. 'I grant you safe passage through my ancestral home,' he "
        "screams in your face, 'and THIS is how you repay me?'",
        "You have no idea why he would be so offended by someone climbing onto his roof, but you never get the "
        "opportunity to find out. The gust of wind from his screaming throws your body like a hockey puck against a low"
        " railing, and you fall... and land with a THUD on the ground far below, crushing all your internal organs in "
        "the process.", "THE END", "Move back 1 space on the Psychic Scale and return to Story Card 53."
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    psych, danger = fifty_three(psych, danger)
    return psych, danger


def forty_four(psych, danger):
    text = [
        "Entering a child's playroom, you find a giant, overstuffed toy box resting against one wall, and in the middle "
        "of the room stands a dollhouse, which appears to be a perfect replica of the Marsden house.",
        "As you approach the dollhouse, you notice that the walls of the playroom are covered with shelves full of "
        "porcelain dolls, their eyes peering down at you. It's difficult to break their gaze. The eyes seem to draw you "
        "into the blackness of their dead stares.",
        "Not looking away, you feel yourself shrinking smaller and smaller. Soon the dolls seem to loom over you, even "
        "more frightening than before, although they never move from their perches. Eventually you're the size of a "
        "doll yourself, and you stand on the playroom floor beside the replica of the Marsden house.",
        "From where you stand you can see the front door of the dollhouse.",
        "Enter the door of the dollhouse by going to Story Card 49."
    ]
    wrap(text)
    psych, danger = forty_nine(psych, danger)
    return psych, danger


def forty_five(psych, danger):
    text = [
        "Most of the books lining the walls of this room appear to be first editions of well-known classics. To help "
        "reach the tallest shelves, there's a wheeled ladder that can slide across the room. A silver door is on one "
        "wall.", "One book -- Introduction to Psychic Dreams, Visions, and Limericks -- catches your eye, and you wheel the "
        "ladder over, climb up, and grab it. As soon as you pull the book from the shelf, a catch releases, and a "
        "hidden door opens on the other side of the room."
    ]
    wrap(text)
    text = [
        "PREMONITION", "If you are Level 2 or higher on the Psychic Scale, draw CLUE 42",
        f"You are {psychLevel(psych)} on the Psychic Scale."
    ]
    wrapFast(text)
    if psych >= 6:
        print('You received a premonition!')
        clue2.forty_two()
    else:
        print('You did not receive the premonition.')
    text = [
        "If you go through the silver door, enter 'fifty eight' to go to Story Card 58",
        "If you go through the hidden door, enter 'forty four' to go to Story Card 44."
    ]
    wrapFast(text)
    options = ('fifty eight', '58', 'forty four', '44')
    choice = choose(options)
    if choice in ['fifty eight', '58']:
        psych, danger = fifty_eight(psych, danger)
    else:
        psych, danger = forty_four(psych, danger)
    return psych, danger


def forty_six(psych, danger):
    text = [
        "You take  the pathway to  a wooden apartment with a quaint front porch. No one appears to be home. You try the "
        "door and find that it's open.",
        "You enter a room that's entirely dark except for one candle-lit corner, where you see a leather desk chair "
        "turned away from you, with someone sitting in it. The chair slowly swivels to reveal a chimpanzee wearing a "
        "monocle and holding a ballpoint pen, looking you square in the eye. Uh-oh. Looks like you interrupted his work.",
        "The chimp calmly places the pen on the desk and removes his monocle. He cracks his knuckles and stands up.",
        "It's Go Time. And this chimp is going for you.", "The chimp pounces!"
    ]
    wrap(text)
    text = [
        "REQUIRED FIGHTING CHALLENGE", "Fight the chimp", "WIN: Lower Danger Meter by five",
        "LOSE: Raise Danger Meter by three"
    ]
    wrapFast(text)
    chal, danger = challenge('required', 'fighting', danger)
    if chal == 'fail':
        print('The chimp bested you!')
        psych, danger = dangerUp(psych, danger, 3)
    else:
        print('You bested the chimp!')
        danger = dangerDown(danger, 5)
    text = [
        "After the fight, the chimp scurries away. You notice to your left there is a large metal door, which looks "
        "completely out of place here. There's also a walkway leading toward what looks like the study in the main house."
    ]
    wrap(text)
    text = [
        "If you open the metal door, enter 'sixty' to go to Story Card 60.",
        "If you take the walkway to the study, enter 'thirty three' to go to Story Card 33."
    ]
    wrapFast(text)
    options = ('sixty', '60', 'thirty three', '33')
    choice = choose(options)
    if choice in ['sixty', '60']:
        psych, danger = sixty(psych, danger)
    else:
        psych, danger = thirty_three(psych, danger)
    return psych, danger


def forty_seven(psych, danger):
    text = [
        "You fumble for a light switch. There is nothing on the walls, but a tiny little chain brushes against your "
        "cheek as you cross the room, so you pull on it. The room floods with light.",
        "This place is well stocked! Bottles of water, stacks of canned food, crates of tools... even boxes labeled "
        "ENTERTAINMENT. This is everything you'd need to survive for weeks.",
        "The only thing out of place is a cabinet painted purple with orange trim. Across the room is an impressive "
        "metal door. Above the door is a hole in the ceiling, which doesn't seem right, given that this place is "
        "supposed to be totally secure."
    ]
    wrap(text)
    text = [
        "If you open the purple and orange cabinet to look inside, enter 'thirty eight' to go to Story Card 38.",
        "If you try to open the big metal door, enter 'sixty' to go to Story Card 60.",
        "If you go up through the hole in the ceiling, enter 'forty four' to draw CLUE 44."
    ]
    wrapFast(text)
    options = ('thirty eight', '38', 'sixty', '60', 'forty four', '44')
    choice = choose(options)
    if choice in ['thirty eight', '38']:
        psych, danger = thirty_eight(psych, danger)
    elif choice in ['forty four', '44']:
        psych, danger = clue2.forty_four(psych, danger)
    else:
        psych, danger = sixty(psych, danger)
    return psych, danger


def forty_eight(psych, danger):
    text = [
        "Once you've entered the solarium, you notice how the glass panes are in angular shapes that create a "
        "spider-web pattern across the ceiling. There are clay pots with exotic plants on every flat surface.",
        "'Welcome,' you hear a female voice say. 'We are so glad you found your way here.'",
        "An elderly woman in a long black dress and white apron glides into view from behind a wall. She appears to be "
        "the housekeeper. She raises one finger and curls it toward her, beckoning you.",
        "'We've been expecting you. Come this way,' she says.",
        "Something in her voice makes you freeze. This might be trouble. You notice something shiny tucked behind a "
        "tropical shrub, but you'll probably have to deal with the housekeeper before you can investigate it. You "
        "glimpse an art gallery beyond the solarium."
    ]
    wrap(text)
    text = [
        "OPTIONAL PERCEPTION CHALLENGE", "Attempt to excuse yourself",
        "(If you are Level 2 or higher on the Psychic Scale, lower your Danger Meter 3 spaces (1 level) for this "
        "challenge only)", "WIN: Draw CLUE 39", "LOSE: Draw CLUE 53", "If you do NOT take the Challenge, continue below."
    ]
    wrapFast(text)
    print(f'  You are {psychLevel(psych)} on the Psychic Scale.')
    if psych >= 6:
        boost = 3
        print('You received a Roll Boost for this Challenge!')
    else:
        boost = 0
        print('You did not receive a Roll Boost for this Challenge.')
    chal, danger = challenge('optional', 'perception', danger - boost)
    if chal == 'fail':
        psych, danger = clue2.fifty_three(psych, danger)
    elif chal == 'win':
        psych, danger = clue2.thirty_nine(psych, danger)
    else:
        text = [
            "If you rudely run away to the art gallery, enter 'thirty two' to go to Story Card 32",
            "If you ignore her and leave through the solarium door, enter 'fifty five' to go to Story Card 55"
        ]
        wrapFast(text)
        options = ('thirty two', '32', 'fifty five', '55')
        choice = choose(options)
        if choice in ['thirty two', '32']:
            psych, danger = thirty_two(psych, danger)
        else:
            psych, danger = fifty_five(psych, danger)
    return psych, danger


def forty_nine(psych, danger):
    text = [
        "The dollhouse entryway has doorways leading to a dining room, a parlor, and a bedroom. Before you can think "
        "about where you should go next, something distracts you. There's a force at work here, a presence you can't "
        "ignore. Something -- or someone -- seems to be calling you, drawing you onward. You can tell: this dollhouse "
        "is a hub of psychic energy, a nexus of weird power. You'll need to stay sharp."
    ]
    wrap(text)
    text = [
        "If you go to the dollhouse dining room, enter 'thirty five' to go to Story Card 35.",
        "If you go to the dollhouse parlor, enter 'fifty seven' to go to Story Card 57.",
        "If you go to the dollhouse bedroom, enter 'forty one' to go to Story Card 41."
    ]
    wrapFast(text)
    options = ('thirty five', '35', 'fifty seven', '57', 'forty one', '41')
    choice = choose(options)
    if choice in ['thirty five', '35']:
        psych, danger = thirty_five(psych, danger)
    elif choice in ['fifty seven', '57']:
        psych, danger = fifty_seven(psych, danger)
    else:
        psych, danger = forty_one(psych, danger)
    return psych, danger


def fifty(psych, danger):
    text = [
        "You enter the bathroom and close the door behind you -- only to jump about three feet in the air when the door "
        "suddenly bulges inward with a loud THUD. Frost spreads across the bathroom mirror, and you stand so still you "
        "almost stop breathing until the frost finally stops spreading. It recedes, and the scary, bulging door returns "
        "to its normal shape.",
        "The bathroom is decorated in various shades of green, and a claw-foot tub sits against one wall. There's a "
        "hatch in the ceiling -- maybe it leads to the attic. You lean out a small window and see a drainpipe on the "
        "house's exterior wall. Leaning out farther, you see another window and through it, paintings on the wall. The "
        "sun is setting, and the rain is really coming down now, so climbing the drainpipe to the gallery would be tricky."
    ]
    wrap(text)
    text = [
        "OPTIONAL CLIMBING CHALLENGE", "Climb down the drainpipe to the window of the art gallery",
        "WIN: Lower Danger Meter by four and go to Story Card 32.", "LOSE: Raise Danger Meter by one and try again.",
        "If you do NOT Take the Challenge, continue below."
    ]
    wrapFast(text)
    chal, danger = challenge('optional', 'climbing', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        while chal == 'fail':
            psych, danger = dangerUp(danger, psych, 1)
            print('Next attempt: ')
            chal, danger = challenge('required', 'climbing', danger)
    if chal == 'win':
        psych, danger = thirty_two(psych, danger)
    text = [
        "Skip the drainpipe and climb up into the ceiling hatch by going to Story Card 53."
    ]
    wrapFast(text)
    psych, danger = fifty_three(psych, danger)
    return psych, danger


def fifty_one(psych, danger):
    text = [
        "You enter a formal dining room decorated in a modern style. The walls are a deep, moody gray, and the table "
        "and chairs are lacquered glossy black. A glass vase containing limp, long-dead flowers sits in the center of "
        "the table.",
        "Around the table sit four men. Their skin and uniforms are all shades of shimmering white and blue, and a "
        "wispy aura wafts off of them like smoke. They're dressed in Civil War-era Union soldier uniforms and talking "
        "as if telling stories around a campfire. One has his feet propped up on the table. They don't seem to be aware "
        "of your presence.",
        "You notice a wooden door that is rattling, as if something behind it is trying to escape. Beams of blue light "
        "shoot out of the keyhole and the wooden slats of the door. There's also a narrow, swinging door at the end of "
        "the dining room that probably leads to the kitchen."
    ]
    wrap(text)
    text = [
        "FREE ACTION", "If you are at Level 2 or higher on the Psychic Scale, and if you want to get closer and listen "
                       "to their stories, draw CLUE 48"
    ]
    wrapFast(text)
    wrapFast([f'You are at {psychLevel(psych)} on the Psychic Scale.'])
    if psych >= 6:
        choice = input('You are high enough level to listen! Would you like to draw CLUE 48? [y/n] ')
        while choice.lower() not in ['y', 'n']:
            choice = input('Please enter y or n: ')
        if choice == 'y':
            clue2.forty_eight()
        else:
            pass
    else:
        print('You are not high enough level to try to listen.')
    text = [
        "If you quietly open the rattling wood door with blue light, go to Story Card 37.",
        "If you sneak past the men and go into the kitchen, go to Story Card 54."
    ]
    wrapFast(text)
    options = ('thirty seven', '37', 'fifty four', '54')
    choice = choose(options)
    if choice in ['thirty seven', '37']:
        psych, danger = thirty_seven(psych, danger)
    else:
        psych, danger = fifty_four(psych, danger)
    return psych, danger


def fifty_two(psych, danger):
    text = [
        "You climb onto the table and wait to descend. Something's wrong -- you begin to go up instead of down. You "
        "rise rapidly and... crash through the skylight! Glass shatters all around you. The lift keeps going up until "
        "you're almost two full stories above the house. The rain is falling so heavily that you're quickly soaked, "
        "and dark clouds roil on the horizon all around you.",
        "You see lightning strike in the distance, and you're filled with horror as you realize you are now on a "
        "towering metal pillar in the middle of a thunderstorm. This is a giant lightning rod!",
        "Lightning strikes the hydraulic lift, and you feel a searing flash of heat as millions of volts pulsate through"
        " your body. The shock forces you to let go of the pole, and before you hit the ground, you black out -- forever.",
        "THE END", "Move back 1 space on the Psychic Scale and return to Story Card 36."
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    psych, danger = thirty_six(psych, danger)
    return psych, danger


def fifty_three(psych, danger):
    text = [
        "After a short climb, you're in the attic. It's dusty and creepy, and there's another ladder here.",
        "This second ladder leads to the roof, but you can see through the window that the storm has really intensified:"
        " it's pouring outside now. YOu poke your head out through the window and discover a stout vine on the outside "
        "wall that could easily support your weight. And most importantly, thanks to a wide overhang, climbing out this "
        "way would keep you dry. You can see through French doors on the ground floor that lead into a study."
    ]
    wrap(text)
    text = [
        "If you climb up the ladder to the roof, enter 'forty three' to go to Story Card 43.",
        "If you climb down the vine to the study, enter 'thirty three' to go to Story Card 33."
    ]
    wrapFast(text)
    options = ('forty three', '43', 'thirty three', '33')
    choice = choose(options)
    if choice in ['forty three', '43']:
        psych, danger = forty_three(psych, danger)
    else:
        psych, danger = thirty_three(psych, danger)
    return psych, danger


def fifty_four(psych, danger):
    text = [
        "The kitchen looks a bit drab, compared to what you've seen of the rest of the house. A large, blue refrigerator"
        " stands lonely against one wall, a heavy chain wrapped around it, holding it closed. THe opposite wall is "
        "dominated by tall cupboards.",
        "Black-and-white checkered tile covers the counter tops and the floors, and a butcher's block on the counter is "
        "stained a deep crimson from heavy use. On the far side of the room there's a small door that appears to lead to"
        " a wine cellar."
    ]
    wrap(text)
    text = [
        "OPTIONAL PERCEPTION CHALLENGE", "Search the cupboards", "WIN: Draw CLUE 34", "LOSE: Raise Danger Meter by one"
    ]
    wrapFast(text)
    check = False
    chal, danger = challenge('optional', 'perception', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print('You failed to find anything in the cupboards.')
        psych, danger = dangerUp(danger, psych, 1)
    else:
        clue2.thirty_four()
        check = True
    text = [
        "OPTIONAL STRENGTH CHALLENGE", "Try to open the fridge", "WIN: Draw CLUE 49", "LOSE: Raise Danger Meter by one."
    ]
    wrapFast(text)
    chal, danger = challenge('optional', 'strength', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print("You weren't able to open the fridge.")
        psych, danger = dangerUp(danger, psych, 1)
    else:
        clue2.forty_nine()
    if not check:
        print("Enter the wine cellar by going to Story Card 56.")
        psych, danger = fifty_six(psych, danger)
    else:
        text = [
            "If you want to enter the wine cellar, enter 'fifty six' to go to Story Card 56.",
            "OR... To follow the secret passage, enter 'fifty nine' to go to Story Card 59."
        ]
        wrapFast(text)
        options = ('fifty six', '56', 'fifty nine', '59')
        choice = choose(options)
        if choice in ['fifty six', '56']:
            psych, danger = fifty_six(psych, danger)
        else:
            psych, danger = fifty_nine(psych, danger)
    return psych, danger


def fifty_five(psych, danger):
    text = [
        "You start to leave, but the woman senses your fear. She smiles again and then begins to fade... You can see "
        "right through her now.",
        "Her shadowy shape wavers and shifts, billowing like a hazy cloud. In seconds, she has taken on a new form -- a "
        "Union general. He has a heavy whip in one hand, and his other hand is clenched into a fist.",
        "The plants around the room grow to become ten feet tall. Even in the darkness you can tell that they are Venus "
        "flytraps. But at this size, they won't be content with flies.",
        "The general has a crazed look in his eyes, as though he's suffering from a sudden fit of rage.",
        "'You think you can challenge the authority of Henry Marsden?', he shouts. He snaps his whip on the floor three "
        "times, and all of the giant Venus flytraps move toward you." "With every shred of his ghostly power, Marsden "
        "snaps the whip at your feet. The force of the violent CRACK is so mighty it sends you sailing backward -- "
        "directly into the maw of one of the hungry plants.",
        "The Venus flytrap takes three quick bites and one slow gulp. You no longer exist.", "THE END",
        "Move back 1 space on the Psychic Scale and return to Story Card 48."
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    psych, danger = forty_eight(psych, danger)
    return psych, danger


def fifty_six(psych, danger):
    text = [
        "The door to the wine cellar is covered with a leather overlay that is embossed with grapevine patterns. "
        "Someone here must really like their wine. You push open the door into a pitch-black room and hear odd noises "
        "coming from some unseen machine in the distance. This space might be bigger than you thought.",
        "As you try to find a light switch, you discover a ladder on your left and a door to your right. As your eyes "
        "adjust to the darkness, you can make out a BOMB SHELTER sticker on the door and a small storage compartment "
        "next to the shelter door, about as tall as your knee."
    ]
    wrap(text)
    text = [
        "FREE ACTION", "If you'd like to get down on your hands and knees and root around in the storage compartment, "
        "draw CLUE 35."
    ]
    wrapFast(text)
    choice = input('Would you like to inspect the storage? [y/n] ')
    while choice.lower() not in ['y', 'n']:
        choice = input('Please enter y or n: ')
    if choice.lower() == 'y':
        clue2.thirty_five()
    text = [
        "If you climb up the ladder, enter 'forty' to draw CLUE 40.",
        "If you go to the bomb shelter, enter 'forty seven' to go to Story Card 47."
    ]
    wrapFast(text)
    options = ('forty', '40', 'forty seven', '47')
    choice = choose(options)
    if choice in ['forty', '40']:
        psych, danger = clue2.forty(psych, danger)
    else:
        psych, danger = forty_seven(psych, danger)
    return psych, danger


def fifty_seven(psych, danger):
    text = [
        "A piano takes up one corner of the dollhouse parlor. A doll sits on a piano bench, wearing a crown and a rich "
        "red gown, hands poised above the keys. This is the doll queen, and even though her back is turned, you feel as "
        "though she's daring you to face her in some kind of bizarre piano contest... of the mind. Perhaps accepting the"
        " queen's unusual challenge -- and defeating her -- will increase your psychic skills.",
        "You notice a painting above the piano. It depicts a solarium and is so spell-bindingly realistic you can't help"
        " but reach out your hand to touch it. You are amazed when your hand disappears into the painting, and you can "
        "touch the solarium on the other side. This painting is a magical portal, and it might be your only way out of "
        "this dollhouse!"
    ]
    wrap(text)
    text = [
        "OPTIONAL PERCEPTION CHALLENGE", "Battle the doll queen in a psychic piano duel", "WIN: Draw CLUE 30",
        "LOSE: Raise Danger Meter by three. You may try again"
    ]
    wrapFast(text)
    chal, danger = challenge('optional', 'perception', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        while chal == 'fail':
            print('You lost to the doll queen!')
            psych, danger = dangerUp(danger, psych, 3)
            choice = input('Would you like to try battling the doll queen again? [y/n] ')
            while choice not in ['y', 'n']:
                choice = input('Please enter y or n: ')
            if choice == 'y':
                chal, danger = challenge('required', 'perception', danger)
            else:
                chal, danger = ''
    else:
        psych = clue2.thirty(psych)
    text = [
        "If you go to the dollhouse dining room, enter 'thirty five' to go to Story Card 35.",
        "If you go to the dollhouse bedroom, enter 'forty one' to go to Story Card 41.",
        "If you have CLUE 50 and you want to enter the magical portal, enter 'forty seven' to draw CLUE 47.",
        "If you do NOT have CLUE 50 and you want to enter the magical portal, enter 'fifty five' to draw CLUE 55."
    ]
    wrapFast(text)
    options = ['thirty five', '35', 'forty one', '41']
    if searchInv('50'):
        print('You have CLUE 50!')
        options.append('forty seven')
        options.append('47')
    else:
        print('You do not have CLUE 50.')
        options.append('fifty five')
        options.append('55')
    choice = choose(options)
    if choice in ['thirty five', '35']:
        psych, danger = thirty_five(psych, danger)
    elif choice in ['forty one', '41']:
        psych, danger = forty_one(psych, danger)
    elif choice in ['fifty five', '55']:
        psych, danger = clue2.fifty_five(psych, danger)
    else:
        psych, danger = clue2.forty_seven(psych, danger)
    return psych, danger


def fifty_eight(psych, danger):
    text = [
        "You find yourself in a hallway with no doors. You notice a stairway down but choose to explore the hallway. "
        "When you reach the end of the hallway, you come to a wall of glass with a glass door set into it, which leads "
        "into a solarium. The door appears to be locked with a strange, intricate mechanism. You inspect the glass -- "
        "it's some kind of special, super-hardened material. Special or not, though, the material is still glass, and "
        "you might be able to break it and enter the solarium."
    ]
    wrap(text)
    text = [
        "If you have CLUE 29, discard it and draw CLUE 46.",
        "If you do NOT have CLUE 29, you MUST take the Challenge below."
    ]
    wrapFast(text)
    if searchInv('29'):
        print('  You have the Glass Key!')
        psych, danger = clue2.forty_six(psych, danger)
    else:
        text = [
            "STRENGTH CHALLENGE", "Smash the glass door", "WIN: Raise Danger Meter by two and draw CLUE 37",
            "LOSE: Raise Danger Meter by two and try again."
        ]
        wrapFast(text)
        chal, danger = challenge('required', 'strength', danger)
        while chal == 'fail':
            print('You failed to smash the glass door!')
            psych, danger = dangerUp(danger, psych, 2)
            chal, danger = challenge('required', 'strength', danger)
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = clue2.thirty_seven(psych, danger)
    return psych, danger


def fifty_nine(psych, danger):
    text = [
        "You enter an extravagantly decorated master bedroom. A dressing table with a fancy mirror sits against one "
        "wall across from a canopy bed covered in burgundy silk.",
        "The ghost of a Union general sits on the bed, facing away from you. As the floor creaks beneath your step, the "
        "ghostly figure turns and leaps to his feet. He has a fearsome scowl on his face and an empty scabbard on his belt.",
        "'Coward! Traitor! Thief!' he yells as he approaches.",
        "There's an open door on the far side of the room, through which you glimpse a bathroom with dark green tiles. "
        "You could also retreat back into the hallway to escape the phantom's wrath."
    ]
    wrap(text)
    text = [
        "FREE ACTION", "If you have CLUE 2 you may attempt to give it to the ghost. To do so, discard it and draw CLUE 32.",
        "If you do not have CLUE 2, continue below."
    ]
    wrapFast(text)
    check = searchInv(2)
    if not check:
        print('  You do not have CLUE 2.')
    while check:
        print('You do have CLUE 2!')
        choice = input('Would you like to give it to the ghost? [y/n] ')
        while choice not in ['y', 'n']:
            choice = input('Please enter y or n: ')
        if choice == 'y':
            psych, danger = clue2.thirty_two(psych, danger)
            check = False
        else:
            check = False
    else:
        text = [
            "OPTIONAL FIGHTING CHALLENGE", "Fight the ghost", "WIN: Draw CLUE 51.", "LOSE: Raise Danger Meter by two."
        ]
        wrapFast(text)
        chal, danger = challenge('optional', 'fighting', danger)
        if chal == 'quit':
            pass
        elif chal == 'fail':
            print('You lost to the ghost!')
            psych, danger = dangerUp(danger, psych, 2)
        else:
            psych, danger = clue2.fifty_one(psych, danger)
        text = [
            "If you run for the bathroom, enter 'fifty' to go to Story Card 50.",
            "If you escape back out into the hallway, enter 'forty' to go to Story Card 40."
        ]
        wrapFast(text)
        options = ('fifty', '50', 'forty', '40')
        choice = choose(options)
        if choice in ['fifty', '50']:
            psych, danger = fifty(psych, danger)
        else:
            psych, danger = forty(psych, danger)
        return psych, danger


def sixty(psych, danger):
    text = [
        "CHAPTER TWO GOAL ACHIEVED",
        "You shove the Metal door open. When you close it behind you -- CLANG -- it sounds like the door to a jail cell "
        "slamming shut. You turn to check out where you are. There's an elevator!",
        "You get in, press the 'Close Door' button, and finally get a moment to catch your breath. You can't believe "
        "what you've been through so far. But this elevator should be your ticket to the basement, and that should bring "
        "you one step closer to uncovering the mystery of the sounds you heard when you first entered the Marsden house. "
        "Now that you know where the elevator is, you wonder if you should go to the basement now, or go back and "
        "investigate anything you might have missed.", "STORY RETURN",
        "There items in this chapter that will be useful later in the story. You can take a risk and go back for any "
        "you missed by following the choices below."
    ]
    wrap(text)
    text = [
        "If you go to the upstairs hallway, raise Danger Meter by two and go to Story Card 39.",
        "If you go to the main dining room, raise Danger Meter by two and go to Story Card 51.",
        "If you go to the solarium, raise Danger Meter by two and go to Story Card 48.",
        "If you go to the gallery, raise Danger Meter by two and go to Story Card 32.",
        "Otherwise you may advance to Chapter Three by entering 'chapter three' (you will keep all inventory items)."
    ]
    wrapFast(text)
    print(f'  Your Danger Meter is at {dangerMeter[danger]} and is {9 - danger} spaces from the top of the scale.')
    print(f'  Your Psychic Scale is at {psych} and is at {psychLevel(psych)}.')
    options = ('thirty nine', '39', 'fifty one', '51', 'forty eight', '48', 'thirty two', '32', 'chapter three')
    choice = choose(options)
    if choice in ['thirty nine', '39']:
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = thirty_nine(psych, danger)
    elif choice in ['fifty one', '51']:
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = fifty_one(psych, danger)
    elif choice in ['forty eight', '48']:
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = forty_eight(psych, danger)
    elif choice in ['thirty two', '32']:
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = thirty_two(psych, danger)
    else:
        return psych, danger
