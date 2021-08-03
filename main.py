from kivy.app import App
from kivy.graphics import Line, Color, Rectangle
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):

    my_text = StringProperty("1")
    count_enabled = BooleanProperty(False)
    switch_enabled = BooleanProperty(False)
    # slider_value_txt = StringProperty("0")
    text_input_str = StringProperty("")

    def on_button_click(self):
        print("Button Clicked!")
        if self.count_enabled == True:
            self.my_text = str(int(self.my_text) + 1)
        else:
            pass

    def on_toggle_button_state(self, widget):
        print("toggle state " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
        if widget.active == True:
            self.switch_enabled = True
        else:
            self.switch_enabled = False

    def on_slider_value(self, widget):
        print("Slider: " + str(widget.value))
        # self.slider_value_txt = str(widget.value)

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class StackLayoutExample(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-bt"
        for i in range(100):
            # size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i + 1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


class CanvasExample1(Widget):
    pass


class CanvasExample4(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=5)
            self.rect = Rectangle(pos=(700, 200), size=(150, 100))

    def on_button_a_click(self):
        print("click works!")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x+w)
        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos = (x, y)


TheLabApp().run()
