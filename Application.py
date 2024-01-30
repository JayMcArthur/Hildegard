import json

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QSpinBox, QLabel, QPushButton, QLineEdit, QWidget, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QCheckBox, QGraphicsWidget, QGraphicsView
from pyqtconfig import ConfigManager, ConfigDialog


# Game will only save AFTER each card. This Means Mid battles will not save
default_player = {
    "Game Type": 1,  # This will be the number of players / Not started game
    "Player_1_type": 0,  # This is which Img you are using and Max Feats
    "Gold": 3,
    "Feats": 0,
    "Inventory": [],
    "Status_Effects": [],  # Which status Effects you are currently afflicted by
    "Player_1_Unlocks": [],  # Which starting cards you have unlocked
    "Player_2_Unlocks": []

}
# These could all be one window with drop downs
# - One display does the Player card with options
# - One displays any Items in a list
# - One displays an item with any options
# One displays the current card
# Special for Fishing or Battles
# One for rolling

default_save = {
    "Name": "Hello",
    "Dinner": 1,
    "Likes": 12.5,
    "RSVP": False,
}

default_save_metadata = {
    "Name": {
        "preferred_handler": QLineEdit
    },
    "Dinner": {
        "preferred_handler": QComboBox,
        "preferred_map_dict": {
            "Chicken": 1,
            "Beef": 2,
            "Fish": 3
        }
    },
    "Likes": {
        "preferred_handler": QSpinBox,
        "prefer_hidden": True
    },
    "RSVP": {
        "preferred_handler": QCheckBox
    }
}


class Application(QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.title = 'Hildegard Digital'
        # This should be a function - Can pass in card number and stuff
        self.setWindowTitle(self.title)
        # We want a Square Ratio Based on screen size
        # then we can find out Card Size based on Screen
        smallest = min(size.width(), size.height())
        self.sizing = {
            # Menu Default: 843px * 843px
            "menu": {
                "height": 843 if smallest >= 843 else smallest,
                "width": 843 if smallest >= 843 else smallest
            },
            # Card Default:  3.5in * 2.5in
            "card": {
                "height": 490 if smallest >= 490 else smallest,
                "width": 350 if smallest >= 490 else int(5*smallest/7)
            }
        }
        self.setMinimumSize(self.sizing['card']['width'], self.sizing['card']['height'])
        self.setMaximumSize(self.sizing['menu']['width'], self.sizing['menu']['height'])

        # This should be a function
        # Also should consider if we are showing any other cards at the time
        self.left = int((size.width() / 2) - (self.sizing['menu']['width'] / 2))
        self.top = int((size.height() / 2) - (self.sizing['menu']['height'] / 2))
        self.setGeometry(self.left, self.top, self.sizing['menu']['width'], self.sizing['menu']['height'])

        self.icon = './images/Icon.ico'
        self.setWindowIcon(QIcon(self.icon))

        self._main = QWidget()
        self.setCentralWidget(self._main)

        self.menu_background = QLabel(parent=self._main)
        self.menu_background.setGeometry(0, 0, self.sizing['menu']['width'], int(self.sizing['menu']['height']*0.9))
        self.menu_background.setObjectName('MenuBackground')
        self.menu_background.setPixmap(QPixmap('./images/main_screen.png'))

        self.start_button = QPushButton(parent=self._main, text="Begin")
        self.start_button.setGeometry(QRect(int(self.sizing['menu']['width']/2 - 168/2), 765, 168, 64))
        self.start_button.setObjectName("StartButton")
        self.start_button.setStyleSheet("background-color: black;")

        # self.layout = QVBoxLayout(self._main)
        self.show()


class Hildegard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """initiates application UI"""

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        """centers the window on the screen"""

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Example(QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.title = 'Hildegard Digital'
        self.width = 600
        self.height = 300
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(size.width(), size.height())
        self.left = int((size.width() / 2) - (self.width / 2))
        self.top = int((size.height() / 2) - (self.height / 2))
        self.setWindowTitle(self.title)
        self.icon = './images/Icon.ico'
        self.setWindowIcon(QIcon(self.icon))

        self._main = QWidget()
        self.setCentralWidget(self._main)
        self.layout = QVBoxLayout(self._main)

        self.current_save = []
        self.save_button = []
        self.saveManagers = []
        for i in range(4):
            self.create_save_handler(i)
            self.current_save[i].setText(str(self.saveManagers[i].as_dict()))

        self.show()

    def create_save_handler(self, number):
        self.current_save.append(QTextEdit())
        self.current_save[number].setReadOnly(True)
        self.save_button.append(QPushButton(f"Settings {number}"))
        self.layout.addWidget(self.current_save[number])
        self.layout.addWidget(self.save_button[number])
        self.saveManagers.append(ConfigManager(default_save, filename=f"saves/save{number}.json"))
        self.saveManagers[number].set_many_metadata(default_save_metadata)
        self.saveManagers[number].updated.connect(self.show_config_creator(number))
        self.save_button[number].clicked.connect(self.create_config_dialog_creator(number))

    def create_config_dialog_creator(self, number):
        def create_config_dialog():
            config_dialog = ConfigDialog(self.saveManagers[number], self, cols=2, flags=Qt.WindowType.WindowCloseButtonHint)
            config_dialog.setWindowTitle(f"Settings {number}")
            config_dialog.setMaximumWidth(400)
            config_dialog.accepted.connect(lambda: self.update_config(config_dialog.config, number))
            config_dialog.exec()
        return create_config_dialog

    def update_config(self, update, number):
        self.saveManagers[number].set_many(update.as_dict())
        self.saveManagers[number].save()

    def show_config_creator(self, number):
        def show_config():
            self.current_save[number].setText(str(self.saveManagers[number].as_dict()))
        return show_config

