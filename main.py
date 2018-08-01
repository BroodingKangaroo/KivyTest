from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout


class BoxApp(App):
    def build(self):
        bl = BoxLayout(size_hint=[0.2, 0.2])
        bl1 = AnchorLayout()
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text="hello"))
        bl1.add_widget(bl)
        return bl1


if __name__ == "__main__":
    BoxApp().run()
