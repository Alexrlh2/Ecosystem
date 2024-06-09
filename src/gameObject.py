import math

import geometry_utils
class GameObject:
    def __init__(self, x, y, radius=7):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def pos(self):
        return (self.x, self.y)

    @pos.setter
    def pos(self, value):
        self.x, self.y = value

    def update(self, world):
        pass

    def collidesWith(self, other: 'GameObject') -> bool:
        return geometry_utils.is_closer_than(self.pos, other.pos, self.radius)

    def can_eat(self, other):
        return False
