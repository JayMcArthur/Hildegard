from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from Application import Application, Hildegard, Example
import qdarktheme as theme
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("Favro Ventures")
    app.setOrganizationDomain("SpiresEnd.com")
    app.setApplicationName("HildegardDigital")
    screen = app.primaryScreen()
    theme.setup_theme()
    customFont = QFont('Arial', 12)
    app.setFont(customFont)
    Hildegard = Example(screen.size())
    sys.exit(app.exec())
