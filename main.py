from kivy.app import App
from kivy.uix.button import Button



class MyClass(App):
    def build(self):
        btn = Button(text = "Оо кнопка!",
                     on_press = self.btn_press)
        return btn
    def btn_press(self,instance):
        instance.text = 'Оо псы!, это вы?'





if __name__ == '__main__':
    MyClass().run()