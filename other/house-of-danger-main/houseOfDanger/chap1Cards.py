from functions import *
import chap1Clues as clue


def one(psych, danger):
    print("Chapter One: The Grounds")
    print()
    text = [
        "It's a Tuesday morning in late June, and you wake up in a cold sweat. The nightmares came again last night. " 
        "Even though you are an aspiring detective and psychic investigator, you haven't been able to make sense of " 
        "the haunting dreams you've had these past few weeks. In your dreams you keep seeing the same spooky house. " 
        "You're still shivering under the covers when you hear the phone ring downstairs in your basement, where" 
        " you have your combination office and research laboratory. You dash down to the lab to answer it."
        "(press enter to continue)",
        '"I need... I need...," a weak voice says when you pick up the receiver. "I need your hel-l-l-lp." You hear a'
        ' loud click, and the phone goes dead.',
        "But you were prepared: while the caller was talking, you activated your high-speed telephone tracking device."
        " It instantly displays the caller's number: 555-7259.",
        "You call back the number right away, but there's no answer. After consulting the tall stack of reverse phone "
        " books behind your desk, you are disappointed to learn the number is unlisted.",
        "You sense that the phone call is somehow related to your nightmares.",
        "Later, while at the Hedge Brook Police Station to return a night scope you borrowed for a recent stakeout,  "
        "you describe the mysterious phone call and your recurring dreams to your friend, Sergeant Morrison.",
        '"That call does sound strange," he says. "We will look into it."',
        '"And about that house in your dreams," a voice says from the hallway. "I wonder if you are dreaming about  '
        'the Marsden house out on Hedge Brook Road." Detective Murphy sticks his mustached face into the room.',
        '"Modern house, ornate gate... That sounds like the Marsden place, all right," says Sergeant Morrison. "Strange'
        '  things are reported to happen out there."',
        'Detective Murphy takes a puff on his pipe. "That place is haunted," he says. "I know it sounds unprofessional,'
        ' but I have had a file on the Marsden house for years, and I am sure of it." He waves a folder in front'
        ' of your eyes, and a phone number written on the front jumps out at you. It matches the one from your '
        'mysterious phone call!',
        "So the call is related to your nightmares -- your psychic sense was right!",
        "Back at home, you grab a bottle of water and your trusty pocketknife, preparing for a new investigation. Half"
        " an hour later, you stand before the Marsden residence, which appears exactly as it did in your nightmares."
        " The house's futuristic look is a strange contrast to the antiquated appearance of the stone wall and the "
        "wrought iron gate, which is locked shut and wrapped in steel chains.",
        "Even though the air is balmy, a chill travels down your spine. The gathering clouds on the horizon hint at a"
        " brewing summer thunderstorm.",
        "If you search the wall for a way in, enter 'thirteen' to go to Story Card 13.",
        "If you climb the gate, enter 'seven' to go to Story Card 7."
    ]

    wrap(text[:11])
    clue.twenty_six()
    wrap(text[11:])
    options = ("thirteen", "seven", '13', '7')
    choice = choose(options)
    if choice in ('thirteen', '13'):
        psych, danger = thirteen(psych, danger)
    else:
        psych, danger = seven(psych, danger)
    return psych, danger


def two(psych, danger):
    text = [
        'In one heroic move, you jump into the opening of the roof access door and land on your feed inside the greenhouse,'
        ' ninja-like. You take a deep breath, ninja-like. You collect yourself, ninja-like. You assess the situation...'
        ' like a ninja',
        "The botanical specimens in this greenhouse are unlike anything you've ever seen. Glossy pink bulbs seven feet "
        "across sit atop yellow vines that spread horizontally for twenty feet. One plant with sharp spikes is actually"
        " see-through."
        "Suddenly, you hear a rustling sound. You look to the corner of the room and see a dark-green cluster of vertical"
        " vine twitching and shaking. 'I might not be alone,' you think."
        "Through the wall of the greenhouse, you spot a commotion of some kind on top of a gazebo just beyond the trees"
        " about forty feet away. You need to think fast!"
        "If you check out the writhing vines, enter 'twenty-five' to go to Story Card 25."
        "If you dash outside to explore the commotion on the gazebo, enter 'nine' to go to Story Card 9."
    ]

    wrap(text)
    options = ('twenty five', 'nine', '9', '25')
    choice = choose(options)
    if choice in ['twenty five', '25']:
        psych, danger = twenty_five(psych, danger)
    else:
        psych, danger = nine(psych, danger)
    return psych, danger


def three(psych, danger, card):
    text = [
        "You only make it a few steps across the open field before you hear a clicking sound from around your feet that"
        " freezes you in your tracks. Looking down, you see freshly disturbed earth around your sneakers, as though "
        "someone had recently buried something there.",
        "As you lift your foot to look -- KA-KLICK! -- the reality of the situation becomes clear. You have just stepped"
        " on a landmine.",
        "A noise like thunder, infinitely loud, rings out, but you never even hear it. Instantly, everything goes black.",
        "THE END",
        "Move back 1 space on the Psychic Scale and return to the previous card."
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    if card == 'fifteen':
        psych, danger = fifteen(psych, danger)
    else:
        psych, danger = nineteen(psych, danger)
    return psych, danger


def four(psych, danger):
    text = [
        "The horseman is a dashing, bearded Civil War soldier, his bronze face stoic. He holds out a cavalry sabre "
        "toward the brooding sky. The sword's edge glints in the weak sunlight that penetrates the thickening clouds "
        "above. The sword looks almost new.", "At the base of the statue is a plaque that proclaims this as a memorial "
        "to Henry Marsden. The plaque reads:", "Henry Marsden, born 1839, died 1887. General in the Union Army during "
        "the Civil War. Severely wounded at the Battle of Shiloh in 1862. Appointed warden of Hedge Brook Prison in "
        "1880.", "To your left is the entrance to a hedge maze. To your right is a graying picket fence with a rickety "
        "wooden gate. You can see two stone angel statues and beyond them, a cemetery.", "Optional Perception Challenge:"
        " Search the monument's base.", "WIN: Draw Clue 18", "LOSE: Raise danger meter by 1"
    ]
    wrap(text)
    options = ['twelve', 'twenty one', '12', '21']
    chal, danger = challenge('optional', 'perception', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        psych, danger = dangerUp(psych, danger, 1)
        print("  You failed to adequately search the monument's base.")
    else:
        clue.eighteen()
        options.append('twenty eight')
        options.append('28')
    text = [
        "Optional Climbing Challenge: Climb the statue to examine the sabre", "WIN: Draw CLUE 2", "LOSE: Raise Danger "
        "Meter by two. You may try again."
    ]
    wrap(text)
    cont = True
    while cont:
        chal, danger = challenge('optional', 'climbing', danger)
        if chal == 'quit':
            cont = False
        elif chal == 'fail':
            psych, danger = dangerUp(psych, danger, 2)
            print("  You failed to adequately search the monument's base.")
            choice = ''
            while choice not in ['y', 'n']:
                choice = input("  Would you like to attempt this challenge again?")
            if choice == 'n':
                cont = False
        else:
            psych = clue.two(psych)
            cont = False
    text = [
        "If you enter the hedge maze, enter 'twelve' to go to Story Card 12.", "If you visit the cemetery, enter "
        "'twenty one' to go to Story Card 21."
    ]
    if '28' in options:
        text.append("OR... If you want to see where the hidden passage leads, enter 'twenty eight' to go to Story Card"
                    " 28.")
    wrap(text)
    choice = choose(options)
    if choice in ['twelve', '12']:
        psych, danger = twelve(psych, danger)
    elif choice in ['twenty eight', '28']:
        psych, danger = twenty_eight(psych, danger)
    else:
        psych, danger = twenty_one(psych, danger)
    return psych, danger


def five(psych, danger):
    text = [
        "The mausoleum interior feels musty and cool. Something is dripping from the ceiling and landing in the corner "
        "with a PLINK, which is odd, given that it hasn't started raining yet. You also notice the mausoleum is bigger"
        " on the inside than you outside suggested. A stone sarcophagus lies before you with the word MARSDEN carved "
        "into it.", "It appears that others have been in the mausoleum recently: there's a freshly dug pit to the side "
        "of the sarcophagus, and an elaborate tunnel has been dug into the ground beside the nearby wall. You can see "
        "that the tunnel is lined with cement.", "Optional Perception Challenge: Search around the sarcophagus", "WIN: "
        "Draw CLUE 23.", "LOSE: Raise Danger meter by one. You may try again."
    ]
    wrap(text)
    cont = True
    while cont:
        chal, danger = challenge('optional', 'perception', danger)
        if chal == 'quit':
            cont = False
        elif chal == 'fail':
            psych, danger = dangerUp(psych, danger, 1)
            print("  You failed to adequately search around the sarcophagus.")
            choice = ''
            while choice not in ['y', 'n']:
                choice = input("  Would you like to attempt this challenge again?")
            if choice == 'n':
                cont = False
        else:
            clue.twenty_three(psych)
            cont = False
    text = [
        "Optional Strength Challenge: Remove the stone lid of the sarcophagus.", "WIN: Draw CLUE 16.", "LOSE: Raise "
        "Danger Meter by 2"
    ]
    wrap(text)
    options = ['sixteen', 'twenty eight', '16', '28']
    chal, danger = challenge('optional', 'strength', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        psych, danger = dangerUp(psych, danger, 2)
        print("  You failed to remove the sarcophagus lid.")
    else:
        clue.sixteen()
        options.append('twenty four')
        options.append('24')
    text = [
        "If you climb into the pit, enter 'sixteen' to go to Story Card 16.", "If you travel through the tunnel, enter "
        "'twenty eight' to go to Story Card 28."
    ]
    wrap(text)
    choice = choose(options)
    if choice in ['sixteen', '16']:
        psych, danger = sixteen(psych, danger, 'five')
    elif choice in ['twenty four', '24']:
        psych, danger = clue.twenty_four(psych, danger)
    else:
        psych, danger = twenty_eight(psych, danger)
    return psych, danger


def six(psych, danger):
    text = [
        "Just as you reach for the doorknob, a fierce gust of wind violently flings open the door. The windows are all "
        "wide open, and wind continues to rush through the quarters, blowing papers off tables and knocking an umbrella"
        " stand to the ground with a CRASH.", "Your arm accidentally knocks a teacup off the kitchen counter, which "
        "shatters on the floor. You start to feel nervous.", "You notice a phone on the wall. This might be too much to"
        " handle alone. You grab the phone and call Sergeant Morrison.", "'Hedge Brook Police Station. Sergeant Morrison"
        " speaking,' he says.", "'Sergeant Morrison!', you blurt out. 'It's me! I'm on the grounds of the Marsden house!"
        " I might be in trouble!'", "'Hello? Hello?', says the sergeant impatiently.", "'It's me!' you shout back. 'I "
        "need your help!'", "'Hello?' Sergeant Morrison says, exasperated. 'Good-bye!'", "He hangs up!", "You are unsure"
        " why the sergeant couldn't hear you, but you are now distracted by a swirl of sounds: a haunting violin plays "
        "somewhere outside, while a wild and chaotic noise rises from a gazebo in the distance.", "If you move in the "
        "direction of the violin, enter 'seventeen' to go to Story Card 17.", "If you check out the gazebo, enter 'nine'"
        " to go to Story Card 9."
    ]
    wrap(text)
    options = ('seventeen', 'nine', '9', '17')
    choice = choose(options)
    if choice in ['seventeen', '17']:
        psych, danger = seventeen(psych, danger)
    else:
        psych, danger = nine(psych, danger)
    return psych, danger

    
def seven(psych, danger):
    text = [
        "You pull yourself over the rusting gate and land with a CRUNCH on the gravel driveway leading toward the house."
        " But before you can survey your surroundings, you hear a guttural sound coming from your left.",
        "You encounter a shadowy, hunched-over figure emerging from the darkened doorway of a decrepit gatehouse. You "
        "can just barely make out eyes and white fangs dripping with saliva.",
        "The figure crouches, as if to spring forward at any moment.",
        "'Who's th-there?' you stammer. Suddenly, the creature lunges at you, snarling. You spot a guardhouse not far "
        "away. If you can get past the creature, you might be able to hide there. Or perhaps you should just turn and "
        "flee up the driveway toward the main house!",
        "Optional Fighting Challenge: Fight the creature.", "WIN: Draw CLUE 10.", "LOSE: Raise Danger Meter by two."
    ]
    wrap(text)
    chal, danger = challenge('optional', 'fighting', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print('  You failed to defeat the creature! Your danger level went up by 2')
        psych, danger = dangerUp(danger, psych, 2)
    else:
        psych, danger = clue.ten(psych, danger)
    text = [
        "If you run into the guardhouse, enter 'nineteen' to go to Story Card 19.",
        "If you run up the driveway, enter 'eight' to go to Story Card 8."
    ]
    wrap(text)
    options = ('nineteen', 'eight', '19', '8')
    choice = choose(options)
    if choice in ['nineteen', '19']:
        psych, danger = nineteen(psych, danger)
    else:
        psych, danger = eight(psych, danger)
    return psych, danger


def eight(psych, danger):
    text = [
        "Your heart pounding, you bolt up the driveway, which bends around the back side of the manor. After running "
        "about fifty yards, you slow down, out of breath. Gasping for air, you stop at a large wall of thorny hedges "
        "lining one side of the driveway. You hear water trickling down a ditch on the opposite side of the driveway. "
        "Charcoal-grey clouds are massing ominously on the horizon, and the nearby tree branches rattle with sudden "
        "gusts of wind.", "Before you can catch your breath, a dark-windowed limousine roars around the bend -- you only"
        " have a split second to decide which way to go to avoid being hit!",
        "If you dash through the hedges, enter 'fifteen' to go to Story Card 15.",
        "If you jump into the ditch, enter 'twenty six' to go to Story Card 26."
    ]
    wrap(text)
    options = ('fifteen', 'twenty six', '15', '26')
    choice = choose(options)
    if choice in ['fifteen', '15']:
        psych, danger = fifteen(psych, danger)
    else:
        psych, danger = twenty_six(psych, danger)
    return psych, danger


def nine(psych, danger):
    text = [
        "You sprint to the gazebo, practically pushed along by the winds that are picking up. A light sprinkling of rain"
        " spatters the ground as you run.",
        "You make it to the shelter of the structure, and the mayhem occurring above you on the roof increases in "
        "intensity.", "'Who is up there and what are they doing?' you wonder.",
        "You notice a driveway about twenty feet away.",
        "PREMONITION: If you are Level 2 or higher on the Psychic Scale, draw CLUE 27."
    ]
    wrap(text)
    if psych >= 6:
        print(f'  You are at place {psych}, on the Psychic Scale, which means you are level two or above!')
        clue.twenty_seven()
    else:
        print(f'  You are at place {psych} on the Psychic Scale, which is not high enough for level two.')
    text = [
        "If you climb to the top of the gazebo, enter 'ten' to go to Story Card 10",
        "If you run to the driveway, enter 'thirty' to go to Story Card 30."
    ]
    wrap(text)
    options = ('ten', 'thirty', '10', '30')
    choice = choose(options)
    if choice in ['ten', '10']:
        psych, danger = ten(psych, danger)
    else:
        psych, danger = thirty(psych, danger)
    return psych, danger


def ten(psych, danger):
    text = [
        "You stand on the gazebo's railing, steadying yourself by gripping an ornate post holding up the roof. The "
        "rumbling above sounds and feels frightening -- what are you getting yourself into?", 
        "Reluctant to barge into the middle of this situation, you raise yourself just enough for a peek and discover "
        "that there is no one on the gazebo roof. The commotion is actually a large satellite dish, broken into three "
        "pieces. The big, jagged fragments are still connected to the base by wires, and the violent winds are spinning"
        " them in a circle with great force.", "Flailing wildly like an angry octopus, the satellite dish almost hits "
        "you in the face. You might be able to grab a piece zooming by.", 
        "Required Climbing Challenge: Attempt to grab a piece of the satellite dish.", 
        "WIN: Draw CLUE 22.", "LOSE: Draw CLUE 17."
    ]
    wrap(text)
    chal, danger = challenge('required', 'climbing', danger)
    if chal == 'fail':
        psych, danger = clue.seventeen(psych, danger)
    else:
        psych, danger = clue.twenty_two(psych, danger)
    return psych, danger


def eleven(psych, danger):
    text = [
        "You can tell that the pool house was once quite luxurious. It contains half a dozen private rooms with showers,"
        " as well as an ornate mahogany bar in the common area. It must have been fun to hang out in this place in its "
        "glory days. Those thoughts fade as the sounds of a disturbance erupt from the top of a gazebo in the distance.",
        "And now you can hear a lone violin playing a soothing melody.",
        "If you go to the gazebo, enter 'nine' to go to Story Card 9.",
        "If you follow the sound of the violin, enter 'seventeen' to go to Story Card 17."
    ]
    wrap(text)
    options = ('nine', 'seventeen', '9', '17')
    choice = choose(options)
    if choice in ['nine', '9']:
        psych, danger = nine(psych, danger)
    else:
        psych, danger = seventeen(psych, danger)
    return psych, danger


def twelve(psych, danger):
    text = [
        "The hedge maze is massive. Its thick hedge walls are twice as tall as you but don't seem stable enough to "
        "climb, so you'll have to solve this labyrinth the old-fashioned way! You take a deep breath to steady your "
        "nerves and head through the maze's entrance.", 
        "If you go left, enter 'nine' to draw CLUE 9.", "If you go right, enter 'one' to draw CLUE 1."
    ]
    wrap(text)
    options = ('nine', 'one', '9', '1')
    choice = choose(options)
    if choice in ['nine', '9']:
        psych, danger = clue.nine(psych, danger)
    else:
        psych, danger = clue.one(psych, danger)
    return psych, danger


def thirteen(psych, danger):
    text = [
        "Moving along the mossy stone wall that surrounds the property, you come across a jagged opening created by "
        "fallen rocks -- it's just big enough for you to squeeze through. Once on the other side of the wall, you find "
        "yourself standing in a cobblestone plaza surrounded by marble and bronze figures. Most of the sculptures depict"
        " men gazing off into the distance as if pondering the deeper meaning of it all, but at the edge of the "
        "courtyard is a monumental statue of a man atop a muscular steed.", 
        "To your right, a stony pathway leads away from the statuary and into a picturesque garden, where topiary bushes"
        " have been trimmed into whimsical shapes.", "If you inspect the statue of the man on the horse, enter 'four' "
        "to go to Story Card 4.", "If you walk toward the topiary bushes, enter 'fifteen' to go to Story Card 15."

    ]
    wrap(text)
    options = ('four', 'fifteen', '4', '15')
    choice = choose(options)
    if choice in ['four', '4']:
        psych, danger = four(psych, danger)
    else:
        psych, danger = fifteen(psych, danger)
    return psych, danger


def fourteen(psych, danger):
    text = [
        "You climb down the gnarled vine into a walled courtyard beside an outbuilding that appears to be the servants' "
        "quarters. The door is slightly ajar, but you are unsure if anyone is inside. In the courtyard there is a small "
        "table with a cigar box sitting on top of it. There is also a path that leads out of the courtyard and up to the"
        " side of the mansion.", "FREE ACTION: To check out what's in the cigar box, draw CLUE 15."

    ]
    wrap(text)
    choice = ''
    while choice not in ['y', 'n']:
        choice = input('  Would you like to inspect the cigar box? [y/n] ')
    if choice == 'y':
        clue.fifteen()
    text = [
        "If you approach the door to the servants' quarters, enter 'six' to go to Story Card 6.",
        "If you run to the side of the mansion, enter 'twenty' to go to Story Card 20."
    ]
    wrap(text)
    options = ('six', 'twenty', '6', '20')
    choice = choose(options)
    if choice in ['six', '6']:
        psych, danger = six(psych, danger)
    else:
        psych, danger = twenty(psych, danger)
    return psych, danger


def fifteen(psych, danger):
    text = [
        "You emerge into a clearing. Manicured bushes in the shapes of fish, swans, and rabbits perch atop a well-kept "
        "lawn. One larger shrub has been sculpted to look like an outstretched hand with its palm upturned. "
        "You see a black handle of some kind sticking up out of one of the fingertips.",
        "A brick path winds through the shrubs and splits into two paths in the distance. One of these leads toward a "
        "rickety wooden gate flanked by a pair of stone angel statues. The other path leads to an open field, "
        "across which you can see the front door of the Marsden manor.",
        "FREE ACTION: To pull the handle out of the bush, draw CLUE 5."
    ]
    wrap(text)
    choice = ''
    while choice not in ['y', 'n']:
        choice = input('  Would you like to pull the handle out of the bush? [y,n] ')
    if choice == 'y':
        clue.five()
    text = [
        "If you walk through the wooden gate, enter 'twenty one' to go to Story Card 21.",
        "If you head across the field toward the manor's front door, enter 'three' to go to Story Card 3."
    ]
    wrap(text)
    options = ('twenty one', 'three', '21', '3')
    choice = choose(options)
    if choice in ['twenty one', '21']:
        psych, danger = twenty_one(psych, danger)
    else:
        psych, danger = three(psych, danger, 'fifteen')
    return psych, danger


def sixteen(psych, danger, card):
    text = [
        "Without warning, the earthen walls begin to collapse around you, and before you can react, you are up to your "
        "waist in dirt. You writhe and twist, trying to escape, but it only causes more soil to cascade down. Soon it's"
        " up to your shoulders, then your neck, then your cheeks. You struggle to spit the soil out as it fills your "
        "mouth, but within moments you are fully buried. You can only see the dark earth in front of your eyes. Your "
        "hand closes around a metal disc -- perhaps a coin? You'll never know, though, as the soil fills your lungs, "
        "and the world wavers and goes grey before finally turning black.", 
        "THE END", "Move back one space on the Psychic Scale and return to the previous card."
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    if card == 'five':
        psych, danger = five(psych, danger)
    elif card == 'twenty one':
        psych, danger = twenty_one(psych, danger)
    else:
        psych, danger = twenty_eight(psych, danger)
    return psych, danger


def seventeen(psych, danger):
    text = [
        "You move further and further toward the hypnotic sound of the distant violin, which is oddly calming and "
        "uplifting even as the winds increase around you.", "You notice there is a driveway up in the distance, but "
        "before you get there, you arrive at a horse stable with an open gate. Inside, sitting on a stool, is the "
        "source of the violin music: a chimpanzee playing his heart out, a soulful expression on his face.", 
        "The chimp is fully committed to the music. You have never heard such an emotional performance.", 
        "It's... it's beautiful.", 
        "If you leave the stable and run to the driveway, enter 'thirty' to go to Story Card 30.", 
        "If you tiptoe through the gate to experience the full power of the performance, enter 'twenty four' to go to "
        "Story Card 24."
    ]
    wrap(text)
    options = ('thirty', 'twenty four', '30', '24')
    choice = choose(options)
    if choice in ['thirty', '30']:
        psych, danger = thirty(psych, danger)
    else:
        psych, danger = twenty_four(psych, danger)
    return psych, danger


def eighteen(psych, danger):
    text = [
        "You finally come to the end of the hedge maze. It exits toward a pool house. A short stone pedestal stands in "
        "front of you with a metal lockbox on top. Perhaps someone wants to reward you for navigating that accursed "
        "maze, though the whole thing does seem suspicious.",
        "Looking toward the pool house, you see its door is barely hanging from its hinges. There is also a gate that "
        "leads -- you assume -- directly to the pool.", "FREE ACTION: To see if the lockbox is open, draw CLUE 3."
    ]
    wrap(text)
    choice = ''
    while choice not in ['y', 'n']:
        choice = input('  Would you like to investigate the lockbox? [y,n] ')
    if choice == 'y':
        psych = clue.three(psych)
    text = [
        "If you explore the pool house, enter 'eleven' to go to Story Card 11.",
        "If you walk through the gate to check out the pool, enter 'twenty three' to go to Story Card 23."
    ]
    wrap(text)
    options = ('eleven', 'twenty three', '11', '23')
    choice = choose(options)
    if choice in ['eleven', '11']:
        psych, danger = eleven(psych, danger)
    else:
        psych, danger = twenty_three(psych, danger)
    return psych, danger


def nineteen(psych, danger):
    text = [
        "You were lucky to escape the creature, but you know it's still out there... somewhere. You run into the old "
        "guardhouse, which is a small room with several TV monitors flashing black-and-white images of various places "
        "on the estate grounds. Some monitors are broken, and shards of glass are scattered across a desk and the wood "
        "floors.", "A hefty book titled History of Nothwin County is lying on the desk. Curious, you look up the name "
        "'Marsden, Henry' in the index. Sure enough, it references an entry on Page 93. Your heart races as "
        "you turn there to read this bio:",
        "Henry Marsden, born 1839, died 1887. General in the Union Army during the Civil War. Severely wounded at the "
        "Battle of Shiloh in 1862. Appointed warden of Hedge Brook Prison in 1880. Rumored to have been killed in the "
        "Prison Riot Fire of 1887.", "'Not a popular guy,' you think.",
        "The desk has three drawers -- maybe there's something useful inside. A wooden ladder leads up to a hatch in "
        "the roof. Through a window filled with cobwebs you can see an open field that leads to the manor's front door. "
        "You consider what to do next.", "Optional Perception Challenge: Search the desk drawers.", "WIN: Draw CLUE 4.",
        "LOSE: Raise Danger Meter by one."
    ]
    wrap(text)
    chal, danger = challenge('optional', 'perception', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print('  You failed to find anything in the drawers.')
        psych, danger = dangerUp(danger, psych, 1)
    else:
        print('  You found something!')
        clue.four()
    text = [
        "If you climb the ladder to the hatch in the roof, enter 'twenty seven' to go to Story Card 27.", 
        "If you crawl through the window and run for the front door of the house, enter 'three' to go to Story Card 3."
    ]
    wrap(text)
    options = ('twenty seven', 'three', '27', '3')
    choice = choose(options)
    if choice in ['three', '3']:
        psych, danger = three(psych, danger, 'nineteen')
    else:
        psych, danger = twenty_seven(psych, danger)
    return psych, danger


def twenty(psych, danger):
    text = [
        "Running along the side of the house, you discover that it is a tight squeeze between the house and the fence. "
        "You almost have to shuffle sideways to make it through, which makes you claustrophobic.", 
        "Out of nowhere, you hear the sound of a lone violin playing a gorgeous, flowing melody, with expert skill and "
        "confidence.", "There is a clearing up ahead, though you are unsure of what lies at its end. And the space you "
        "are in has become so tight, it would be easier to climb over the fence to check out the "
        "violinist playing that amazing melody.", "If you run toward the clearing, enter 'thirty' to go to Story Card 30.", 
        "If you climb over the fence to follow the violin melody, enter 'seventeen' to go to Story Card 17."
    ]
    wrap(text)
    options = ('thirty', 'seventeen', '30', '17')
    choice = choose(options)
    if choice in ['seventeen', '17']:
        psych, danger = seventeen(psych, danger)
    else:
        psych, danger = thirty(psych, danger)
    return psych, danger


def twenty_one(psych, danger):
    text = [
        "Passing between a pair of stone angels, you enter an old family cemetery. There is a marble mausoleum in the "
        "center of the cemetery. A short set of stairs leads into its shadowy interior.",
        "Next to where you stand, a freshly dug grave yawns in the pale sunlight. It's unsettling to think of climbing "
        "into it, but you see something shiny embedded in the dirt walls.",
        "If you enter the mausoleum, enter 'five' to go to Story Card 5.",
        "If you climb into the open grave, enter 'sixteen' to go to Story Card 16."
    ]
    wrap(text)
    options = ('five', 'sixteen', '5', '16')
    choice = choose(options)
    if choice in ['five', '5']:
        psych, danger = five(psych, danger)
    else:
        psych, danger = sixteen(psych, danger, 'twenty one')
    return psych, danger


def twenty_two(psych, danger):
    text = [
        "Mustering all the courage you can, you dive into the watery tunnel. There is just enough room in the tunnel "
        "above the water for you to lift your head between strokes and take a breath.",
        "Eventually the tunnel drops lower and lower until it's completely submerged under water. You hold your breath,"
        " dive down, and look around: after about thirty feet, the tunnel opens up to a bigger body of water -- a pond"
        " or pool -- with sunlight beaming into it. You pop up for air. 'Well, I've come this far,' you think. You're "
        "ready to chance it. You take a deep breath and dive back down.",
        "You get ten feet in... fifteen feet in... twenty-five feet in... Just as you're about to exit the underwater "
        "tunnel, something tugs at your leg. You can't tell if it's an animal or if you're caught in an underwater vine.",
        "Required Fighting Challenge: Fight to escape!", "WIN: Draw CLUE 20.",
        "LOSE: Raise Danger Meter by four and try again."
    ]
    wrap(text)
    chal, danger = challenge('required', 'fighting', danger)
    while chal == 'fail':
        print('You failed to escape! Your Danger Meter went up by 4.')
        psych, danger = dangerUp(danger, psych, 4)
        chal, danger = challenge('required', 'fighting', danger)
    psych, danger = clue.twenty(psych, danger)
    return psych, danger


def twenty_three(psych, danger):
    text = [
        "It's obvious that nobody has cleaned the pool in ages. The water is a murky green, and the surface is littered"
        " with leaves and branches. Ripples pulse outward from the center of the pool.",
        "Out of nowhere, you hear a commotion. You look around and wonder if it's coming from inside the pool house "
        "nearby. Then you see movement on top of a gazebo in the distance. Someone -- or something -- is engaged in a "
        "struggle up there. Maybe they need your help! Then again, if you offer assistance you might end up needing "
        "help yourself!", "Optional Perception Challenge: Investigate the ripples in the pool",
        "WIN: Lower Danger Meter by two and draw CLUE 8.", "LOSE: Raise Danger Meter by two. You may try again."
    ]
    wrap(text)
    chal, danger = challenge('optional', 'perception', danger)
    while chal == 'fail':
        print('  You failed to find the source of the ripples! Your danger meter was raised by two.')
        psych, danger = dangerUp(danger, psych, 2)
        choice = ''
        while choice not in ['y', 'n']:
            choice = input('Would you like to attempt to investigate the pool again?')
        if choice == 'n':
            chal, danger = ''
        else:
            chal, danger = challenge('optional', 'perception', danger)
    if chal == 'win':
        psych = clue.eight(psych)
    text = [
        "If you go to the pool house, enter 'eleven' to go to Story Card 11.", 
        "If you go straight to the action at the gazebo, enter 'nine' to go to Story Card 9."
    ]
    wrap(text)
    options = ('nine', 'eleven', '9', '11')
    choice = choose(options)
    if choice in ['nine', '9']:
        psych, danger = nine(psych, danger)
    else:
        psych, danger = eleven(psych, danger)
    return psych, danger


def twenty_four(psych, danger):
    text = [
        "You tiptoe through the open gate, eager to hear the finale of the chimp's violin piece. Quietly... quietly...",
        "With your third step, you trigger a motion-sensor light that completely illuminates the interior of the "
        "building. Apparently, this is no stable: it's a kennel. Twenty Doberman Pinschers were peacefully enjoying the"
        " concert, but now they glare at you with anger in their eyes.",
        "The chimp frowns and slowly points his violin bow towards you. The Dobermans respond and rush to attack you "
        "and then eat you alive. The last thing you see is the chimpanzee violinist laughing at your fate. So embarrassing!",
        "THE END", "Move back 1 space on the Psychic Scale and return to Story Card 17."
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    psych, danger = seventeen(psych, danger)
    return psych, danger


def twenty_five(psych, danger):
    text = [
        "As soon as you take a step toward the vines, one of them lashes out and wraps around your neck. Then another "
        "whips around your waist. More and more vines spring out at you.", "'This isn't really happening,' you think.",
        "The vines are moving all around you, spinning you into a cocoon. You struggle to break free of them, but they "
        "only tighten their grip on you. 'This can't be real!' Eventually, you can't breathe. Everything seems to turn "
        "a deep green, then you see a bright white light -- and then you no longer exist.", "THE END",
        "Move back 1 space on the Psychic Scale and return to Story Card 2."
    ]
    wrap(text)
    psych = dePsych(psych, 1)
    psych, danger = two(psych, danger)
    return psych, danger


def twenty_six(psych, danger):
    text = [
        "You land in the ditch, splashing into shallow, frigid water. At this point, you notice a large grate ahead of "
        "you, which partially blocks the entrance to a dark, cement culvert that the water flows into. If you bent over,"
        " you could walk under the lower rim of the grate and enter the culvert.",
        "You then see a small piece of paper drifting by you in the water. You might be able to grab it if you act fast.",
        "Optional Perception Challenge: Grab the paper", "WIN: Draw CLUE 19.", "LOSE: Raise Danger Meter by one."
    ]
    wrap(text)
    chal, danger = challenge('optional', 'perception', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print(' You failed to grab the paper! Your danger meter went up by 1')
        psych, danger = dangerUp(danger, psych, 1)
    else:
        psych = clue.nineteen(psych)
    text = [
        "Along the side of the ditch is a dusty path leading toward what appears to be an elaborate hedge maze.", 
        "If you enter the culvert, enter 'twenty eight' to go to Story Card 28.", 
        "If you enter the hedge maze, enter 'twelve' to go to Story Card 12."
    ]
    wrap(text)
    options = ('twenty eight', 'twelve', '28', '12')
    choice = choose(options)
    if choice in ['twelve', '12']:
        psych, danger = twelve(psych, danger)
    else:
        psych, danger = twenty_eight(psych, danger)
    return psych, danger

    
def twenty_seven(psych, danger):
    text = [
        "You scramble up the ladder, through the hatch, and onto the guardhouse's decaying roof. It seems to be on the "
        "verge of collapsing, but you find a spot that you are reasonably sure won't cave in when you put your weight on it.",
        "Across the dangerously unstable roof from where you crouch uneasily, you can see a pile of construction "
        "materials, probably left over by contractors working on the roof. Among the material is a first aid kit, but "
        "navigating the length of the roof to reach it will be perilous. One wrong step and you could stumble off the "
        "roof, into a ditch you see below.",
        "Near you is a thick vine that you could climb down to reach a courtyard, and not too far from you is a long "
        "board someone has laid between the roof and a nearby greenhouse, which seems to be sturdier than the guardhouse.",
        "Optional Dexterity Challenge: Get to the first aid kit", "WIN: Draw CLUE 6, then make Story Choice.",
        "LOSE: Raise Danger Meter by two and go to Story Card 26."
    ]
    wrap(text)
    chal, danger = challenge('optional', 'dexterity', danger)
    if chal == 'quit':
        pass
    elif chal == 'fail':
        print('  You fell into the ditch! Your Danger Meter was raised by 2')
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = twenty_six(psych, danger)
    else:
        clue.six()
    text = [
        "If you cross to the greenhouse, enter 'twenty nine' to go to Story Card 29.",
        "If you climb down the vine, enter 'fourteen' to go to Story Card 14."
    ]
    wrap(text)
    options = ('twenty nine', 'fourteen', '29', '14')
    choice = choose(options)
    if choice in ['twenty nine', '29']:
        psych, danger = twenty_nine(psych, danger)
    else:
        psych, danger = fourteen(psych, danger)
    return psych, danger


def twenty_eight(psych, danger):
    text = [
        "You creep through the darkness and find the cement walls end as natural stone and earth begin. Occasional vents"
        " to the surface let in just barely enough light to see by. Ahead you glimpse the warm firelight of torches.", 
        "You come to a fork in the tunnel, lit by the dancing flames. One tunnel descends deeper and is half-filled with"
        " water. You could swim through it, but you can't see where the tunnel leads or how far it goes.", 
        "Another tunnel looks partially caved in. Tiny clumps of earth periodically fall from the ceiling as you "
        "approach this tunnel, and several of the supports that hold the walls up have gaping cracks in them.", 
        "If you dive into the water-filled tunnel, enter 'twenty two' to go to Story Card 22.", 
        "If you explore the partially collapsed tunnel, enter 'sixteen' to go to Story Card 16."
    ]
    wrap(text)
    options = ('twenty two', 'sixteen', '22', '16')
    choice = choose(options)
    if choice in ['twenty two', '22']:
        psych, danger = twenty_two(psych, danger)
    else:
        psych, danger = sixteen(psych, danger, 'twenty eight')
    return psych, danger


def twenty_nine(psych, danger):
    text = [
        "After crossing the precarious board, you find yourself at one end of a walkway that spans the length of the "
        "greenhouse roof. From here you can see most of the mansion's vast grounds, which are a little out of place "
        "amid the surrounding suburban neighborhood. The air is full of mosquitoes and other buzzing insects. The "
        "clouds you saw on the horizon earlier seem to be closer now. You see that there's an open access door in the "
        "roof that would allow you to descend into the greenhouse. You can also drop down onto a path, which appears to"
        " lead to the side of the mansion itself.", "If you wriggle through the access door and enter the greenhouse, "
                                                    "enter 'two' to go to Story Card 2.", 
        "If you drop onto the path and run to the side of the house, enter 'twenty' to go to Story Card 20."
    ]
    wrap(text)
    options = ('two', 'twenty', '2', '20')
    choice = choose(options)
    if choice in ['two', '2']:
        psych, danger = two(psych, danger)
    else:
        psych, danger = twenty(psych, danger)
    return psych, danger

    
def thirty(psych, danger):
    text = [
        "CHAPTER ONE GOAL ACHIEVED", 
        "You appear in a driveway, which leads you to the mansion's entrance. On the door is a plaque that reads "
        "MARSDEN and a large crystal doorknocker, which seems newer than everything else on the front of the building. "
        "You knock loudly, many times. But there is no answer. The storm is really picking up now. You try the doorknob "
        "and are surprised to find that the door is unlocked.", 
        "You've been lucky enough so far, but you wonder if you've missed something. Before you enter the house, you "
        "look back. You can see a few clear paths. One leads toward a statuary, another to a small cemetery. Two more "
        "paths stretch out toward a watery ditch with a gate and the house's luxurious pool. You could go back to "
        "explore if you want.", "STORY RETURN", 
        "There are items in this chapter that will be useful later in the story. You can take a risk and go back for "
        "any you missed by following the choices below.", 
        "If you head the statuary, raise Danger Meter by two and enter 'four' to go to Story Card 4.", 
        "If you head to the cemetery, raise Danger Meter by two and enter 'twenty one' to go to Story Card 21.", 
        "If you head to the ditch, raise Danger Meter by two and enter 'twenty six' to go to Story Card 26.", 
        "If you head to the pool, raise Danger Meter by two and enter 'twenty three' to go to Story Card 23.", 
        "Otherwise, you may advance to Chapter Two by entering 'Chapter Two'. You will keep all of your inventory items."
    ]
    wrap(text)
    options = ('four', 'twenty one', 'twenty six', 'twenty three', '4', '21', '26', '23', 'Chapter Two')
    choice = choose(options)
    if choice in ['four', '4']:
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = four(psych, danger)
    elif choice in ['twenty one', '21']:
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = twenty_one(psych, danger)
    elif choice in ['twenty six', '26']:
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = twenty_six(psych, danger)
    elif choice in ['twenty three', '23']:
        psych, danger = dangerUp(danger, psych, 2)
        psych, danger = twenty_three(psych, danger)
    else:
        pass
    return psych, danger
