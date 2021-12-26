import physics
from physics import *


class Player:
    pos = Pair(0, 0)
    LENGTH, WIDTH, TERM_VELOCITY = 0, 0, 10
    velocity = 0

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
        #if abs(self.velocity <= self.TERM_VELOCITY):
        self.velocity += 1

    def accel_left(self):
        #if abs(self.velocity <= self.TERM_VELOCITY):
        self.velocity -= 1

    def move_player(self):
        if self.TERM_VELOCITY >= self.velocity >= -self.TERM_VELOCITY:
            self.pos.x += self.velocity

    def jump(self):
        physics.jump(self)
