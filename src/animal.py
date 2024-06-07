from gameObject import GameObject


import math
from typing import Tuple
class Animal(GameObject):
    """Animal is a GameObject that has methods for animal stuff like moving around in the world

    Attributes:
        angle   This is the clockwise angle in degrees where 0 = 360 means the animal is facing north
        speed   The speed at which the animal is travelling in the direction it is facing where 0 is not moving, 1 is full speed, and -1 is full speed backwards"""

    speed_scaler = 10
    def __init__(self, x, y, angle: float = 0,energy=100, radius=10):
        super().__init__(x,y, radius)

        self.angle = angle
        self.energy = energy
        self.speed = 0.5

    def update(self, world):
        self.decide_movement()
        self.move()
        self.deplete_energy()
        self.wrap_around_world(world.width, world.height)

    """Implement to adjust speed and direction before the animal takes its step"""
    def decide_movement(self):
        pass
    def move(self):
        dx, dy = self.get_move_vector()
        self.x, self.y =  self.x + dx, self.y +dy

    def get_move_vector(self) -> Tuple[float, float]:
        return (
            (self.speed * self.speed_scaler) * math.cos(90 - self.angle),
            (self.speed * self.speed_scaler) * math.sin(90-self.angle))

    def wrap_around_world(self, world_width, world_height):
        self.x = self.x % world_width
        self.y = self.y % world_height

    """Override to deplete energy each update. Refer to speed to make energy depletion dependent on movement"""
    def deplete_energy(self):
        pass
