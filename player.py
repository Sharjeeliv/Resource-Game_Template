import physics
from physics import *


class Player:
    pos = Pair(0, 0)
    LENGTH, WIDTH, VELOCITY = 0, 0, 2

    def __init__(self, x, y, length, width):
        self.pos.x = x
        self.pos.y = y
        self.LENGTH = length
        self.WIDTH = width

    def object(self):
        return self.pos.x, self.pos.y, self.LENGTH, self.WIDTH

    def get_pair(self):
        return self.pos

    def move_right(self):
        self.pos.x += self.VELOCITY

    def move_left(self):
        self.pos.x -= self.VELOCITY

    def jump(self):
        physics.jump(self)
