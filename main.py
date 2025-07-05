from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class Screen1(MDScreen):
  pass
    
class Screen2(MDScreen):
    pass
        
class MainApp(MDApp):
    key  = ["","",""]
    
    def build(self):
      return super().build()
    
MainApp().run()
