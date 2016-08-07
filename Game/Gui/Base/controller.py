from Gui.Base.widget import Widget


class ButtonPressedController:
    def __init__(self, widget: Widget):
        self.widget = widget
        for i in range(len(self.widget.buttons)):
            func = self.__getattribute__("button{}_on_click".format(i))
            self.widget.buttons[i].clicked.connect(func)


class MousePressedController:
    def __init__(self, widget: Widget):
        self.widget = widget
        self.widget.mousePressEvent = self.__getattribute__("widget_on_pressed")

    def widget_on_pressed(self, e):
        pass