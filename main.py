from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (450, 300)
Window.clearcolor = (76 / 34, 6 / 255, 3 / 255, 1)
Window.title = "Конвертер"

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Конвертер')
        self.miles = Label(text='Мили')
        self.metres = Label(text='Метры')
        self.santimetres = Label(text='Сантиметры')
        self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.miles.text = 'Мили: ' + str(float(data) * 0.62)
            self.metres.text = 'Метры: ' + str(float(data) * 1000)
            self.santimetres.text = 'Сантиметры: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.metres)
        box.add_widget(self.santimetres)

        return box
if __name__ == "__main__":
    MyApp().run()