import os, sys
import random

import pygame
import pygame_gui
from const import *
# Card importers
from cards.chapter_1.loader import chapter1loader
from cards.chapter_2.loader import chapter2loader
from cards.chapter_3.loader import chapter3loader
from cards.chapter_4.loader import chapter4loader
from cards.bows_and_breakfast.loader import bowsAndBreakfastLoader, waffledLoader, calledToArmsLoader
from cards.crows_and_crawdads.loader import crowsAndCrawdadsLoader
from cards.great_outdoors.loader import greatOutdoorsLoader
from cards.oaks_crossing.loader import oaksCrossingLoader

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption('Hildegard')
screen = pygame.display.set_mode(SCREEN_SIZE)
background_color = pygame.Color('#000000')

manager = pygame_gui.UIManager(SCREEN_SIZE)  # Maybe add theme.json
manager.add_font_paths('agency', "other/christmas_adventure/data/AGENCYB.TTF")
manager.preload_fonts([{'name': 'agency', 'point_size': 12, 'style': 'regular'},
                       {'name': 'gabriola', 'point_size': 18, 'style': 'bold'},
                       {'name': 'gabriola', 'point_size': 18, 'style': 'italic'}])


# Setup Scenes if necessary
scenes = []


class SceneOne:
    def __init__(self):
        super().__init__()
        self.background = pygame.Surface(SCREEN_SIZE)
        self.background.fill(pygame.Color(background_color))

    def render_back(self, screen):
        pass

    def render_front(self, screen):
        pass


scene_1 = SceneOne()
scenes.append(scene_1)
active_scene = scenes[0]

text_h = TextHandler()


def setup_ui(_ui_scene_text, text, id=""):
    _ui_scene_text = pygame_gui.elements.UITextBox(text, pygame.Rect((10, 10), (SCREEN_SIZE[0] - 20, SCREEN_SIZE[1] - 40)), manager=manager, object_id=id)


class game_state:
    def __init__(self):
        self.state = GAME_STATES.begin
        self.last_command_bad = False
        self.volume = 50
        self.packs = {
            "chapter_1": True,
            "chapter_2": True,
            "chapter_3": True,
            "chapter_4": True,
            "bows_and_breakfast": False,
            "call_to_arms": False,
            "waffled": False,
            "crows_and_crawdads": False,
            "great_outdoors": False,
            "oaks_crossing": False

        }
        self.equipment = []
        self.feats = 0
        self.status_effects = []
        self.gold = 0
        self.deck = {}
        self.last_card = []
        self.current_card = 0
        self.card_id = 0
        self.character_enabled = False
        self.card_part = 0
        self.card_part_old = -1
        self.preprocess = []

    def process(self, command):
        while len(self.preprocess) > 0:
            effect_list = self.preprocess[0]
            for effect in effect_list:
                self.action(effect[0], effect[1])
            self.preprocess.pop(0)

        if self.last_command_bad:
            self.last_command_bad = False
            if self.deck == {}:
                return text_h.state_to_text(self.state, self.volume, self.packs, None, None)
            return text_h.state_to_text(self.state, self.volume, self.packs, self.deck[f"{self.current_card}"][self.card_id], self.card_part)[1]

        if self.state == GAME_STATES.begin:
            self.state = GAME_STATES.main_menu
            return text_h.MAIN_MENU
        elif self.state == GAME_STATES.main_menu:
            if command not in ['1', '2', '3', '4']:
                self.last_command_bad = True
                return text_h.bad_command
            if command == "1":
                self.pack_loader()
                self.create_character()
                self.state = GAME_STATES.in_game
                return self.load_card(1, "random")
            elif command == "2":
                self.state = GAME_STATES.load_game
                return "TODO - Load Game"
            elif command == "3":
                self.state = GAME_STATES.settings
                return text_h.get_settings(self.volume)
            else:
                pygame.quit()
                sys.exit()
        elif self.state == GAME_STATES.settings:
            if command not in ['1', '2', '3']:
                self.last_command_bad = True
                return text_h.bad_command
            if command == "1":
                self.state = GAME_STATES.volume
                return text_h.VOLUME_MENU
            elif command == "2":
                self.state = GAME_STATES.change_packs
                return text_h.get_packs(self.packs)
            elif command == "3":
                self.state = GAME_STATES.main_menu
                return text_h.MAIN_MENU
        elif self.state == GAME_STATES.volume:
            try:
                command = int(command)
            except ValueError:
                self.last_command_bad = True
                return text_h.bad_command
            if not(0 <= command <= 100):
                self.last_command_bad = True
                return text_h.bad_command
            self.volume = command
            self.state = GAME_STATES.settings
            return text_h.get_settings(self.volume)
        elif self.state == GAME_STATES.change_packs:
            if command not in ["1", "2", "3", "4", "5", "6", "7"]:
                self.last_command_bad = True
                return text_h.bad_command
            if command == "1":
                self.packs["bows_and_breakfast"] = not(self.packs["bows_and_breakfast"])
                self.packs["call_to_arms"] = self.packs["bows_and_breakfast"]
                self.packs["waffled"] = self.packs["bows_and_breakfast"]
            elif command == "2":
                self.packs["call_to_arms"] = not(self.packs["call_to_arms"])
            elif command == "3":
                self.packs["waffled"] = not(self.packs["waffled"])
            elif command == "4":
                self.packs["crows_and_crawdads"] = not (self.packs["crows_and_crawdads"])
            elif command == "5":
                self.packs["great_outdoors"] = not (self.packs["great_outdoors"])
            elif command == "6":
                self.packs["oaks_crossing"] = not (self.packs["oaks_crossing"])
            elif command == "7":
                self.state = GAME_STATES.settings
                return text_h.get_settings(self.volume)
            return text_h.get_packs(self.packs)
        elif self.state == GAME_STATES.in_game:
            if self.card_part < len(self.deck[f"{self.current_card}"][self.card_id]["text"]):
                processed = text_h.card_to_text(self.deck[f"{self.current_card}"][self.card_id], self.card_part + 1)
                self.card_part_old = self.card_part
                self.card_part = processed[0]
                for i in range(self.card_part_old + 1, min(self.card_part + 1, len(self.deck[f"{self.current_card}"][self.card_id]["text"]))):
                    self.preprocess.append(self.deck[f"{self.current_card}"][self.card_id]["text"][i]["effect"])
                return processed[1]
            if len(self.deck[f'{self.current_card}'][self.card_id]['choice']) == 0:
                first_time = False
                self.current_card, self.card_id, self.card_part, self.card_part_old = self.last_card.pop()
                if self.card_part == -1:
                    self.card_part = 0
                    first_time = True
                processed = text_h.card_to_text(self.deck[f"{self.current_card}"][self.card_id], self.card_part)
                if first_time:
                    self.card_part_old = self.card_part
                    self.card_part = processed[0]
                    for i in range(self.card_part_old + 1, min(self.card_part + 1, len(self.deck[f"{self.current_card}"][self.card_id]["text"]))):
                        self.preprocess.append(self.deck[f"{self.current_card}"][self.card_id]["text"][i]["effect"])
                return processed[1]
            if command not in [f'{x}' for x in range(1, len(self.deck[f'{self.current_card}'][self.card_id]['choice'])+1)]:
                self.last_command_bad = True
                return text_h.bad_command
            command = int(command) - 1
            command_action = self.deck[f'{self.current_card}'][self.card_id]['choice'][command]
            for action in command_action["effect"]:
                self.action(action[0], action[1])
            self.load_card(command_action['goto_card'], command_action["pull_type"])

    def parse(self, text):
        # TODO - Make this filter maybe? Or something advanced for other game states
        return text

    def pack_loader(self):
        self.deck = chapter1loader(self.deck)
        self.deck = chapter2loader(self.deck)
        self.deck = chapter3loader(self.deck)
        self.deck = chapter4loader(self.deck)
        if self.packs['bows_and_breakfast']:
            self.deck = bowsAndBreakfastLoader(self.deck)
        if self.packs['call_to_arms']:
            self.deck = calledToArmsLoader(self.deck)
        if self.packs['waffled']:
            self.deck = waffledLoader(self.deck)
        if self.packs['crows_and_crawdads']:
            self.deck = crowsAndCrawdadsLoader(self.deck)
        if self.packs['great_outdoors']:
            self.deck = greatOutdoorsLoader(self.deck)
        if self.packs['oaks_crossing']:
            self.deck = oaksCrossingLoader(self.deck)

    def create_character(self, data=None):
        if data:
            self.equipment = data["equipment"]
            self.deck = data["deck"]
            self.feats = data["feats"]
            self.gold = data["gold"]
            self.last_card = data["last_card"]
            self.current_card = data["current_card"]
        else:
            pass

    def action(self, action, data):
        if action == "gain_gold":
            self.gold += data
        elif action == "gain_feat":
            self.feats += data
        elif action == "interrupt_pull_card":
            self.last_card.append([self.current_card, self.card_id, self.card_part, self.card_part_old])
            self.current_card = data
            self.card_id = 0
            self.card_part = -1
            self.card_part_old = -1
        elif action == "gain_equip":
            self.equipment.append(data)
        elif action == "interrupt_encounter":
            # TODO - Make encounter
            pass
        elif action == "enable_character":
            self.character_enabled = True
        elif action == "interrupt_face_off":
            # TODO - Make Face off
            pass

    def load_card(self, card, load_type):
        card_id = 0
        self.current_card = card
        if load_type == "random":
            card_id = random.randrange(len(self.deck[f"{card}"]))
        self.card_id = card_id
        self.card_part_old = -1
        processed = text_h.card_to_text(self.deck[f"{card}"][card_id], 0)
        self.card_part = processed[0]
        for i in range(self.card_part_old + 1, min(self.card_part + 1, len(self.deck[f"{card}"][card_id]["text"]))):
            self.preprocess.append(self.deck[f"{card}"][card_id]["text"][i]["effect"])
        return processed[1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ui_scene_text = pygame_gui.elements.UITextBox("", pygame.Rect((0, 0), (0, 0)))
    player_text_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((20, SCREEN_SIZE[1] - 30), (SCREEN_SIZE[0] - 30, 25)), manager=manager, object_id="#player_input")
    setup_ui(ui_scene_text, text_h.INTRO)
    game = game_state()

    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        frameTime = clock.tick(60)
        time_delta = frameTime / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                entered_keys = event.text
                parsed_command = game.parse(entered_keys) # Need to make Parse Command
                command_reaction = game.process(parsed_command)
                ui_scene_text.kill()
                setup_ui(ui_scene_text, command_reaction)
                player_text_entry.set_text("")

        manager.set_focus_set({player_text_entry})

        # active_scene.update(time_delta)
        manager.update(time_delta)
        screen.blit(active_scene.background, (0, 0))

        active_scene.render_back(screen)
        manager.draw_ui(screen)
        active_scene.render_front(screen)

        pygame.display.flip()
