from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from random import randint

# Main widget
class PongGame(Widget):
    ball = ObjectProperty(None)
    playerLeft = ObjectProperty(None)
    playerRight = ObjectProperty(None)

    def serve_ball(self, vel = (4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()
        self.playerLeft.bounce_ball(self.ball)
        self.playerRight.bounce_ball(self.ball)

        if(self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.playerRight.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.playerLeft.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.playerLeft.center_y = touch.y
        if touch.x > self.width - self.width/3:
            self.playerRight.center_y = touch.y

# Ball widget
class PongBall(Widget):
    velocity_x = NumericProperty(10)
    velocity_y = NumericProperty(10)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Player(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

# called when app is started
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
    
if __name__ == '__main__':
    PongApp().run()
