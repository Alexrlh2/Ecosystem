import math

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
        distance = math.hypot(self.x - other.x, self.y - other.y)
        return distance < (self.radius + other.radius)

    def can_eat(self, other):
        return False
