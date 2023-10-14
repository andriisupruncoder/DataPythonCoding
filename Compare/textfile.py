from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    MDTextField:
        id: my_text_field

    MDLabel:
        text: "The text of the text field is: " + my_text_field.text
'''


class MyApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen


MyApp().run()