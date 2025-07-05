from kivy.app import MDApp
from kivy.uix.screenmanager import MDScreen

class Screen1(Screen):
  pass
    
class Screen2(Screen):
    pass
        
class MainApp(App):
    key  = ["","",""]
    
    def build(self):
      
      self.theme_cls.primary_palette = "Blue"
      self.theme_cls.theme_style = "Light"
      return super().build()
    
MainApp().run()
