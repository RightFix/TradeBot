from kivy.app import App
from pybit.exceptions import FailedRequestError
from kivy.uix.screenmanager import Screen
from assets.backend import code

class Screen1(Screen):
  pass
    
class Screen2(Screen):
    pass
        
class MainApp(App):
    key  = ["","",""]
    
    def build(self):
      #self.theme_cls.primary_palette = "Blue"
      #self.theme_cls.theme_style = "Light
      
      return super().build()
    def switch(instance,value):
        try:
          orders = code.trading(value[0],value[1],value[2])
          change_to_string = "?".join(orders)
          return change_to_string.replace("?","\n\n")
          
        except FailedRequestError:
           orders  = "Turn On VPN Or No Internet Connection"
           return orders
    
MainApp().run()
