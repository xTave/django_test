from sys import exit
from PyQt5.QtWidgets import QApplication
from Gui.MainMenu.main_menu_widget import MainMenuWidget
from Gui.Window.window import create_window

app = QApplication([""])
app.setQuitOnLastWindowClosed(True)
app.setStyle("Fusion")
create_window(MainMenuWidget())
exit(app.exec())