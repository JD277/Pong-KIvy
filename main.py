# --------------Importing libraies--------------
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
# --------------Importing libraies--------------


# --------------Ball--------------
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

# --------------Ball--------------

# --------------Pong game--------------
class PongGame(Widget):
    ball = ObjectProperty(None)
    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    def update(self,dt):
        self.ball.move()

        if(self.ball.y < 0) or (self.ball.y > self.height):
            self.ball.velocity_y *= -1

        if(self.ball.x < 0) or (self.ball.x > self.width):
            self.ball.velocity_x *= -1
# --------------Pong game--------------

# --------------Pong App--------------

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0)
        return game
# --------------Pong App--------------

PongApp().run()
