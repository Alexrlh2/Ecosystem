import random

from gameObject import GameObject
from plant import Plant


class Herbivore(GameObject):
    speed_scaler = 5

    def __init__(self, x, y, size=10):
        super().__init__(x, y, size)
        self.x_speed = random.uniform(-0.5, 0.5)
        self.y_speed = random.uniform(-0.5, 0.5)

    def update(self, world):
        self.change_speed()
        self.move()
        self.wrap_around_world(world.width, world.height)

        self.try_eat(world.get_objects())

    def change_speed(self):
        self.x_speed = max(-1, min(1, self.x_speed + random.choice((-0.1, 0.1)))) * 0.98
        self.y_speed = max(-1, min(1, self.y_speed + random.choice((-0.1, 0.1)))) * 0.98

    def move(self):
        self.x += self.x_speed * self.speed_scaler
        self.y += self.y_speed * self.speed_scaler

    def wrap_around_world(self, world_width, world_height):
        self.x = self.x % world_width
        self.y = self.y % world_height

    def can_eat(self, other):
        return type(other) is Plant

    def try_eat(self, objects):
        for obj in objects:
            if self.can_eat(obj):
                if self.collidesWith(obj):
                    objects.remove(obj)
                    self.x_speed *= 5
                    self.y_speed *= 5
