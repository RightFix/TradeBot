from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class Screen1(MDScreen):
  pass
    
class Screen2(MDScreen):
    pass
        
class MainApp(MDApp):
    key  = ["","",""]
    
    def build(self):
      
      self.theme_cls.primary_palette = "Blue"
      self.theme_cls.theme_style = "Light"
      return super().build()
    
MainApp().run()
