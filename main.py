# --------------Importing libraies--------------
from kivy.app import App # Create an app instance to build the window
from kivy.uix.widget import Widget # Is all the features that are placed on the app
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty # Are made to keep the compatibility between the laguages
from kivy.vector import Vector # Make possible to move the widgets
from kivy.clock import Clock # Update the screen of the app
from random import randint # Generate random intgeers numbers 
# --------------Importing libraies--------------



# --------------Paddle--------------
class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self,ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1
# --------------Paddle--------------
# --------------Ball--------------
class PongBall(Widget):

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y) # Is the velocity's vector 
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos # Increase the ball position in 4 sixty times per second

# --------------Ball--------------

# --------------Pong game--------------
class PongGame(Widget):
    ball = ObjectProperty(None) # Is the instance of the ball to communicate the .py and .kv files to update the properties of the ball
    pĺayer1 = ObjectProperty(None)
    pĺayer2 = ObjectProperty(None)
    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360)) # Rotates the ball randomly to move it in any direction

    def update(self,dt):
        self.ball.move() 

        # Bounce the ball on top and bottom 
        if(self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1

        # Bounce the ball on left and right direction
        if(self.ball.x < 0):
            self.ball.velocity_x *= -1
            self.player1.score += 1 
        if (self.ball.x > self.width - 50):
            self.ball.velocity_x *= -1 
            self.player2.score += 1 
        
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
    def on_touch_move(self,touch):
        if touch.x < self.width / 1/4:
            self.player1.center_y = touch.y 
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y
# --------------Pong game--------------

# --------------Pong App--------------

class PongApp(App):
    def build(self):
        game = PongGame() # An instance of the PongGame
        game.serve_ball() # Preparing the start direction of the ball
        Clock.schedule_interval(game.update,1.0/60.0) # Update the game 60 per seconds
        return game
# --------------Pong App--------------

PongApp().run()
