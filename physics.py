# This class is primarily for utility and convenience for working with cords and points
class Pair:
    x, y = None, None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def top_offset(self, y):
        return self.y - y

    def height(self):
        return self.y

    def width(self):
        return self.x

    def pair(self):
        return self.x, self.y


def jump(object):
    pass


def gravity(object1, object2):
    if object1.colliderect(object2):
        pass
