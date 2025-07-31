from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class SudokuGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 9
        self.rows = 9
        for i in range(81):
            self.add_widget(TextInput(multiline=False, halign="center", font_size=24))

class SudokuApp(App):
    def build(self):
        return SudokuGrid()

if __name__ == '__main__':
    SudokuApp().run()
