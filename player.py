from physics import Pair
from static import *
from pygame import draw
from time import sleep


class Player:
    pos = Pair(0, 0)
    velocity_x, velocity_y = 0, 0
    player_object = None

    def __init__(self, x, y, length, width):
        self.pos.x = x
        self.pos.y = y
        self.LENGTH = length
        self.WIDTH = width

    def object(self):
        return self.pos.x, self.pos.y, self.LENGTH, self.WIDTH

    def accel_right(self):
        if self.velocity_x < TERM_VELOCITY_X:
            self.velocity_x += RATE

    def accel_left(self):
        if self.velocity_x > -TERM_VELOCITY_X:
            self.velocity_x -= RATE

    def velocity_decay(self):
        if self.velocity_x > 0:
            self.velocity_x -= RATE / 2
        elif self.velocity_x < 0:
            self.velocity_x += RATE / 2

    def move_player(self):
        self.pos.x += self.velocity_x
        self.pos.y += self.velocity_y
        self.velocity_decay()

    def fall(self, other_object):
        if self.player_object.colliderect(other_object):
            self.pos.y -= self.velocity_y
            self.velocity_y = 0
        elif self.velocity_y < TERM_VELOCITY_Y:
            self.velocity_y += RATE

    def jump(self, other_object):
        if self.player_object.colliderect(other_object):
            self.velocity_y = -JUMP_HEIGHT
            self.pos.y += self.velocity_y
            sleep(0.1)  # Delay on how quickly jump can be triggered

    def draw_player(self, screen):
        self.player_object = draw.rect(screen, ORANGE, self.object())
