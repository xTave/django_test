from Gui.Base.widget import Widget
from Gui.MainMenu.main_menu_view import MainMenuView
from Gui.MainMenu.main_menu_controller import MainMenuController


class MainMenuWidget(Widget):
    def __init__(self):
        super().__init__(0, 4, 2, MainMenuView, MainMenuController)