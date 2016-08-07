import sys
from Gui.Base.controller import ButtonPressedController


class MainMenuController(ButtonPressedController):
    def button0_on_click(self):
        from Gui.NewGameMenu.new_game_widget import NewGameWidget
        from Gui.Window.window import set_central_widget
        set_central_widget(NewGameWidget())

    def button1_on_click(self):
        print("Load")

    def button2_on_click(self):
        print("Options")

    def button3_on_click(self):
        sys.exit(0)