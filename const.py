from enum import IntEnum


class WILD_SHOT_TYPES(IntEnum):
    BULLSEYE = 0
    INSTINCT = 1
    RICOCHET = 2
    MISS = 3
    WHOOPSIE = 4


class SHOT_DICE_PARTS(IntEnum):
    BLACK_HALF = 0
    WHITE_HALF = 1
    OUTSIDE_HALF = 2
    CIRCLE = 3
    DOT = 4
    MISS = 5


WILD_SHOT_DICE = {
    "BLACK": [WILD_SHOT_TYPES.BULLSEYE, WILD_SHOT_TYPES.BULLSEYE, WILD_SHOT_TYPES.MISS, WILD_SHOT_TYPES.MISS, WILD_SHOT_TYPES.MISS, WILD_SHOT_TYPES.WHOOPSIE],
    "GRAY": [WILD_SHOT_TYPES.BULLSEYE, WILD_SHOT_TYPES.BULLSEYE, WILD_SHOT_TYPES.RICOCHET, WILD_SHOT_TYPES.MISS, WILD_SHOT_TYPES.MISS, WILD_SHOT_TYPES.WHOOPSIE],
    "GOLD": [WILD_SHOT_TYPES.BULLSEYE, WILD_SHOT_TYPES.BULLSEYE, WILD_SHOT_TYPES.INSTINCT, WILD_SHOT_TYPES.MISS, WILD_SHOT_TYPES.MISS, WILD_SHOT_TYPES.WHOOPSIE],
    "BLUE": [WILD_SHOT_TYPES.BULLSEYE, WILD_SHOT_TYPES.BULLSEYE, WILD_SHOT_TYPES.INSTINCT, WILD_SHOT_TYPES.RICOCHET, WILD_SHOT_TYPES.MISS, WILD_SHOT_TYPES.WHOOPSIE]
}

SHOT_DICE = [
    SHOT_DICE_PARTS.BLACK_HALF,
    SHOT_DICE_PARTS.WHITE_HALF,
    SHOT_DICE_PARTS.OUTSIDE_HALF,
    SHOT_DICE_PARTS.CIRCLE,
    SHOT_DICE_PARTS.DOT,
    SHOT_DICE_PARTS.MISS
]

SHOT_DICE_COMBINATIONS = {
    "BLACK": [SHOT_DICE_PARTS.BLACK_HALF, SHOT_DICE_PARTS.BLACK_HALF],
    "MIXED": [SHOT_DICE_PARTS.BLACK_HALF, SHOT_DICE_PARTS.WHITE_HALF],
    "WHITE": [SHOT_DICE_PARTS.WHITE_HALF, SHOT_DICE_PARTS.WHITE_HALF],
    "CIRCLE-DOT": [SHOT_DICE_PARTS.CIRCLE, SHOT_DICE_PARTS.DOT],
    "OUTSIDE-DOT": [SHOT_DICE_PARTS.OUTSIDE_HALF, SHOT_DICE_PARTS.DOT, SHOT_DICE_PARTS.OUTSIDE_HALF]
}

STATUS_EFFECTS = {
    "HONE": {
        "effect_text": "Add 1 Shot Dice on next Set",
        "effect": [["add_temp_dice", 1]]
    },
    "WILD": {
        "effect_text": "May Reroll a Wild Shot on Set",
        "effect": [["add_wildshot_reroll", 1]]
    },
    "BULLSEYE": {
        "effect_text": "Add 1 Bullseye on a Target or Face-Off",
        "effect": [["get_bullseye", 1]]
    },
    "RESET": {
        "effect_text": "Add 1 additional Set on Target",
        "effect": [["add_set", 1]]
    },
    "REDO": {
        "effect_text": "Retry a Target or Face-Off",
        "effect": [["reset_fight"]]
    },
    "FLUB": {
        "effect_text": "Minus 1 Shot Dice on next Set",
        "effect": [["add_temp_dice", -1]]
    },
    "TAME": {
        "effect_text": "No Wild Shot on next Set",
        "effect": [["remove_wild_shot"]]
    },
    "GRAZE" : {
        "effect_text": "No Finesse on next Set",
        "effect": [["remove_Finesse"]]
    },
    "HIT": {
        "effect_text": "Instant Hit in Face-Off (on Hildegard's Hit Meter)",
        "effect": [["take_damage", 1]]
    }
}

FEATS_OF_MARKSMANSHIP_COSTS = {
    "HONE": 1,
    "WILD": 1,
    "BULLSEYE": 2,
    "RESET": 2,
    "REDO": 3,
    "BLOCK": 1
}


def calculate_available_bullseyes(_BULLSEYE_PARTS_AVAILABLE):
    available = []
    for key, bullseye in SHOT_DICE_COMBINATIONS.items():
        check = all(item in bullseye for item in _BULLSEYE_PARTS_AVAILABLE)
        if check:
            available.append(key)
    return available


class Encounter:
    def __init__(self, _NAME, _BULLSEYE_LIMIT, _ACCURACY, _SETS, _REWARDS, _BONUS_CHALLENGE, _BONUS_REWARD, _BULLSEYE_PARTS_AVAILABLE, _RESULT_PROMPTS):
        self.name = _NAME
        self.bullseye_limit = _BULLSEYE_LIMIT
        self.accuracy = _ACCURACY
        self.sets = _SETS
        self.rewards = _REWARDS
        self.bonus_challenge = _BONUS_CHALLENGE
        self.bonus_reward = _BONUS_REWARD
        self.bullseyes_available = calculate_available_bullseyes(_BULLSEYE_PARTS_AVAILABLE)
        self.results = _RESULT_PROMPTS

    def gain_reward(self):
        for reward in self.rewards:
            [reward_type, reward_amount] = reward
            call_action(reward_type, [reward_amount])

    def gain_bonus_reward(self):
        [reward_type, reward_amount] = self.bonus_reward
        call_action(reward_type, [reward_amount])


ENCOUNTERS = {
    "Midnight Squirrel": Encounter("Midnight Squirrel", 3, 4, 2, [["gain_equip", "Midnight Squirrel Pelt"]], ["Combination", [SHOT_DICE_PARTS.BLACK_HALF, SHOT_DICE_PARTS.BLACK_HALF, SHOT_DICE_PARTS.WHITE_HALF, SHOT_DICE_PARTS.DOT]], ["gain_gold", 2], [SHOT_DICE_PARTS.BLACK_HALF, SHOT_DICE_PARTS.WHITE_HALF], ["resume"])
}

ACTION_KEYS = [
    "gain_gold",
    "gain_feat",
    "interrupt_pull_card",
    "gain_equip",
    "interrupt_encounter",
    "enable_character",
    "start_game"
]

EQUIP_KEYS = [
    "Silver Cap",
    "Compass",
    "Slingshot",
    "Black Wild Shot",
    "Mysterious Package"
]

DECK_KEYS = [
    "chapter_1",
    "chapter_2",
    "chapter_3",
    "chapter_4",
    "bows_and_breakfast",
    "call_to_arms",
    "waffled"
    "crows_and_crawdads",
    "great_outdoors",
    "oaks_crossing"
]

DECK_NAMES = {
    "chapter_1": "Main Game",
    "chapter_2": "Main Game",
    "chapter_3": "Main Game",
    "chapter_4": "Main Game",
    "bows_and_breakfast": "Bows & Breakfast",
    "crows_and_crawdads": "Crows & Crawdads",
    "great_outdoors": "Great Outdoors",
    "oaks_crossing": "Oaks Crossing"
}

SCREEN_SIZE = (705, 987)
TEXT_CENTER = 82


class GAME_STATES(IntEnum):
    begin = 0
    main_menu = 1
    settings = 2
    volume = 3
    change_packs = 4
    in_game = 6
    target = 7
    face_off = 8
    town = 9


class TextHandler:
    def __init__(self):
        self.__title_color = '#4d96f0'
        self.__title = "Spire\'s End - Hildegard".center(TEXT_CENTER)
        self.__title2 = "A Text Adaptation".center(TEXT_CENTER)
        self.__TITLE_COMPLETE = f"<font color='{self.__title_color}'>{self.__title}</font><br>" \
                              f"<font color='{self.__title_color}'>{self.__title2}</font><br>"

        self.__copyright_color = '#FF0000'
        self.__copyright_favro = "\U000000A9 2022, Favro Ventures, All Rights Reserved".center(TEXT_CENTER)
        self.__copyright_jay = "Text Adaptation 2023, Jay McArthur, All Rights Reserved".center(TEXT_CENTER)
        self.__COPYRIGHT_COMPLETE = f"<font color='{self.__copyright_color}'>{self.__copyright_favro}</font><br>" \
                                  f"<font color='{self.__copyright_color}'>{self.__copyright_jay}</font><br>"

        self.__begin_color = '#00FF00'
        self.__intro_begin = "Press Enter to begin".center(TEXT_CENTER)
        self.INTRO = f"{'<br>'*5}{self.__TITLE_COMPLETE}{'<br>' * 2}" \
                     f"{self.__COPYRIGHT_COMPLETE}{'<br>' * 2}" \
                     f"<font color='{self.__begin_color}'>{self.__intro_begin}</font><br>"

        self.__menu_color = '#00FF00'
        self.__main_menu_1 = "1 - New Game".center(TEXT_CENTER)
        self.__main_menu_2 = "2 - Load Game".center(TEXT_CENTER)
        self.__main_menu_3 = "3 - Settings".center(TEXT_CENTER)
        self.__main_menu_4 = "4 - Exit Game".center(TEXT_CENTER)
        self.MAIN_MENU = f"{'<br>'*5}{self.__TITLE_COMPLETE}{'<br>' * 3}" \
                          f"<font color='{self.__menu_color}'>{self.__main_menu_1}</font>{'<br>' * 1}" \
                          f"<font color='{self.__menu_color}'>{self.__main_menu_2}</font>{'<br>' * 1}" \
                          f"<font color='{self.__menu_color}'>{self.__main_menu_3}</font>{'<br>' * 1}" \
                          f"<font color='{self.__menu_color}'>{self.__main_menu_4}</font>{'<br>' * 3}"

        self.__bad_color = '#FF0000'
        self.__bad_command_text = "Invalid Command".center(TEXT_CENTER)
        self.bad_command = f"{'<br>'*7}<font color='{self.__bad_color}'>{self.__bad_command_text}</font>{'<br>' * 1}"

        self.__settings_1 = None
        self.__settings_2 = None
        self.__settings_3 = None
        self.__SETTING_MENU = None

        self.__volume = "Enter desired volume (0-100)".center(TEXT_CENTER)
        self.VOLUME_MENU = f"{'<br>'*5}{self.__TITLE_COMPLETE}{'<br>' * 3}" \
                          f"<font color='{self.__menu_color}'>{self.__volume}</font>{'<br>' * 1}"

        self.__main_deck = None
        self.__bows_and_breakfast = None
        self.__call_to_arms = None
        self.__waffled = None
        self.__crows_and_crawdads = None
        self.__great_outdoors = None
        self.__oaks_crossing = None
        self.__PACKS = None

    def state_to_text(self, state, volume, packs, card, part):
        if state == GAME_STATES.main_menu:
            return self.MAIN_MENU
        elif state == GAME_STATES.settings:
            return self.get_settings(volume)
        elif state == GAME_STATES.volume:
            return self.VOLUME_MENU
        elif state == GAME_STATES.change_packs:
            return self.get_packs(packs)
        elif state == GAME_STATES.in_game:
            return self.card_to_text(card, part)

    def get_settings(self, volume):
        self.__settings_1 = f"1 - Volume {volume}%".center(TEXT_CENTER)
        self.__settings_2 = "2 - Deck Editor".center(TEXT_CENTER)
        self.__settings_3 = "3 - Back".center(TEXT_CENTER)
        self.__SETTING_MENU = f"{'<br>' * 5}{self.__TITLE_COMPLETE}{'<br>' * 3}" \
                            f"<font color='{self.__menu_color}'>{self.__settings_1}</font>{'<br>' * 1}" \
                            f"<font color='{self.__menu_color}'>{self.__settings_2}</font>{'<br>' * 1}" \
                            f"<font color='{self.__menu_color}'>{self.__settings_3}</font>{'<br>' * 1}"
        return self.__SETTING_MENU

    def get_packs(self, packs):
        self.__main_deck = f"x - Main Deck:"
        self.__main_deck = f"{self.__main_deck:<25}[X]".center(TEXT_CENTER)
        self.__bows_and_breakfast = f"1 - Bows & Breakfast:"
        self.__bows_and_breakfast = f"{self.__bows_and_breakfast:<25}[{'X' if packs['bows_and_breakfast'] else ' '}]".center(TEXT_CENTER)
        self.__call_to_arms = f"2 - - - Called to Arms:"
        self.__call_to_arms = f"{self.__call_to_arms:<25}[{'X' if packs['call_to_arms'] else ' '}]".center(TEXT_CENTER)
        self.__waffled = f"3 - - - Waffled:"
        self.__waffled = f"{self.__waffled:<25}[{'X' if packs['waffled'] else ' '}]".center(TEXT_CENTER)
        self.__crows_and_crawdads = f"4 - Crows & Crawdads:"
        self.__crows_and_crawdads = f"{self.__crows_and_crawdads:<25}[{'X' if packs['crows_and_crawdads'] else ' '}]".center(TEXT_CENTER)
        self.__great_outdoors = f"5 - Great Outdoors:"
        self.__great_outdoors = f"{self.__great_outdoors:<25}[{'X' if packs['great_outdoors'] else ' '}]".center(TEXT_CENTER)
        self.__oaks_crossing = f"6 - Oak's Crossing:"
        self.__oaks_crossing = f"{self.__oaks_crossing:<25}[{'X' if packs['oaks_crossing'] else ' '}]".center(TEXT_CENTER)
        self.__settings_3 = "7 - Back".center(TEXT_CENTER)
        self.__PACKS = f"{'<br>' * 5}{self.__TITLE_COMPLETE}{'<br>' * 3}" \
                       f"<font color='{self.__menu_color}'>{self.__main_deck}</font>{'<br>' * 1}" \
                       f"<font color='{self.__menu_color}'>{self.__bows_and_breakfast}</font>{'<br>' * 1}" \
                       f"<font color='{self.__menu_color}'>{self.__call_to_arms}</font>{'<br>' * 1}" \
                       f"<font color='{self.__menu_color}'>{self.__waffled}</font>{'<br>' * 1}" \
                       f"<font color='{self.__menu_color}'>{self.__crows_and_crawdads}</font>{'<br>' * 1}" \
                       f"<font color='{self.__menu_color}'>{self.__great_outdoors}</font>{'<br>' * 1}" \
                       f"<font color='{self.__menu_color}'>{self.__oaks_crossing}</font>{'<br>' * 1}" \
                       f"<font color='{self.__menu_color}'>{self.__settings_3}</font>{'<br>' * 1}"
        return self.__PACKS

    def card_to_text(self, card, part):
        part_new = part
        working_text = ""
        working_text += self.__TITLE_COMPLETE + f"{'<br>' * 3}"
        texts = card["text"]
        options = card["choice"]
        for txt_id, text in enumerate(texts):
            if part_new >= txt_id:
                if part_new == txt_id:
                    if text['auto_continue']:
                        part_new += 1
                broken_txt = text['content'].split('\n')
                for txt_part in broken_txt:
                    txt_part = txt_part.center(TEXT_CENTER)
                    working_text += f"<font color='{text['content_color']}'>{txt_part}</font>{'<br>' * 1}"
                working_text += f"{'<br>' * 1}"

                if txt_id + 1 == len(texts) and part == txt_id + 1:
                    working_text += f"{'<br>' * 2}"
                    for choice_id, option in enumerate(options):
                        txt_part = f"{choice_id + 1} - {option['name']}".center(TEXT_CENTER)
                        working_text += f"<font color='{option['color']}'>{txt_part}</font>{'<br>' * 1}"
            else:
                break

        return [part_new, working_text]

