from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout


class ESP32_InterfaceApp(App):
    def build(self):
        float = FloatLayout()
        scatter = Scatter()
        label = Label(text='Hello World',  
                      font_size=150)
        
        float.add_widget(scatter)
        scatter.add_widget(label)
        return float

if __name__ == '__main__':
    ESP32_InterfaceApp().run()