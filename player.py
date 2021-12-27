import physics
from colours import *
from pygame import draw


class Player:
    pos = physics.Pair(0, 0)
    LENGTH, WIDTH, TERM_VELOCITY_X, RATE, TERM_VELOCITY_Y = 0, 0, 10, 1, 20
    velocity_x, velocity_y = 0, 0
    player_object = None

    def __init__(self, x, y, length, width):
        self.pos.x = x
        self.pos.y = y
        self.LENGTH = length
        self.WIDTH = width

    def object(self):
        return self.pos.x, self.pos.y, self.LENGTH, self.WIDTH

    def get_pair(self):
        return self.pos

    def accel_right(self):
        if self.velocity_x < self.TERM_VELOCITY_X:
            self.velocity_x += self.RATE

    def accel_left(self):
        if self.velocity_x > -self.TERM_VELOCITY_X:
            self.velocity_x -= self.RATE

    def velocity_decay(self):
        if self.velocity_x > 0:
            self.velocity_x -= self.RATE / 2
        elif self.velocity_x < 0:
            self.velocity_x += self.RATE / 2

    def move_player(self):
        self.pos.x += self.velocity_x
        self.velocity_decay()

    def fall(self, object2):
        if self.player_object.colliderect(object2):
            self.pos.y -= self.velocity_y
            self.velocity_y = 0
        elif self.velocity_y < self.TERM_VELOCITY_Y:
            self.velocity_y += self.RATE

        self.pos.y += self.velocity_y

    def draw_player(self, screen):
        self.player_object = draw.rect(screen, ORANGE, self.object())
