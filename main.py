from kivymd.app import MDApp
# from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class Main_Screen(Screen):
    pass
class Screen_2(Screen):
    pass
class Screen_3(Screen):
    pass
class sm(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        # return Builder.load_file("main.kv")
        # return Builder.load_string(KV)
        return

MainApp().run()