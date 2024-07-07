import math
from typing import Tuple

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

    def collides_with(self, other: 'GameObject') -> bool:
        return geometry_utils.is_closer_than(self.pos, other.pos, self.radius)

    def get_relative_distance_and_angle(self, other: 'GameObject') -> Tuple[float, float]:
        """Gets the distance to other and the angle self would need turn to face it in radians"""
        distance = geometry_utils.get_distance_between(self.pos, other.pos)
        dx, dy = other.x - self.x, other.y - self.y
        angle = math.atan2(dy, dx)
        return distance, angle
