from Gui.Base.controller import ButtonPressedController


class NewGameController(ButtonPressedController):
    def button0_on_click(self):
        from Gui.MainMenu.main_menu_widget import MainMenuWidget
        from Gui.Window.window import set_central_widget
        set_central_widget(MainMenuWidget())