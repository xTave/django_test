from Gui.Base.controller import MousePressedController
from Gui.Window.window import set_central_widget
from Gui.Map.map import MapGui, Map


class ChooseStartController(MousePressedController):
    def widget_on_pressed(self, e):
        set_central_widget(MapGui(Map(0, 100)))