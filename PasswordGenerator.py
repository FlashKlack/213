import kivy

from random import sample
from sys import setrecursionlimit
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import ScreenManager, Screen


setrecursionlimit(10000)
kivy.require('2.2.0')
firsts = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?./`"
Window.size = (400, 600)


KV = '''
<MyRoot>:
    random_label: random_label
    BoxLayout:
        orientation: "vertical"
        Label:
            size_hint: 1, 0.15
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            text: "Generator Password"
            font_size: 30
            color: 0, 0.62, 0.96
        Label:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            id: random_label
            text: "PASSWORD"
            font_size: 30
            color: 0, 0.62, 0.96
        Button:
            size_hint: 1, 0.3
            text: "Generate"
            font_size: 25
            on_press: root.create_pass()
'''


class MyRoot(Screen):
    name = 'main'

    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)

    def create_pass(self):
        """Делает пароль"""
        length = 15
        self.random_label.text = ''.join(sample(firsts, length))
        Clipboard.copy(self.random_label.text)


class PasswordGenerator(MDApp):
    theme = ThemeManager
    title = 'Password Generator'

    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager()
        sm.add_widget(MyRoot())
        self.theme.theme_style = 'Dark'
        return sm


if __name__ == '__main__':
    PasswordGenerator().run()
