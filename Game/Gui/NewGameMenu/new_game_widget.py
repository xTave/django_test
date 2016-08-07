from Gui.Base.widget import Widget
from Gui.NewGameMenu.new_game_controller import NewGameController
from Gui.NewGameMenu.new_game_view import NewGameView


class NewGameWidget(Widget):
    def __init__(self):
        super().__init__(6, 1, 0, NewGameView, NewGameController)