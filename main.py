# --------------Importing libraies--------------
from kivy.app import App
from kivy.uix.widget import Widget
# --------------Importing libraies--------------

# --------------Pong game--------------
class PongGame(Widget):
    pass
# --------------Pong game--------------

# --------------Pong App--------------

class PongApp(App):
    def build(self):
        return PongGame()
# --------------Pong App--------------

PongApp().run()
