import random

from gameObject import GameObject
from plant import Plant


class Herbivore(GameObject):
    speed_scaler = 10

    def __init__(self, x, y, energy=100, size=10):
        super().__init__(x, y, size)

        self.energy = energy

        self.x_speed = random.uniform(-0.5, 0.5)
        self.y_speed = random.uniform(-0.5, 0.5)

    def update(self, world):
        self.change_speed()
        self.move()
        self.wrap_around_world(world.width, world.height)

        self.try_eat(world.get_objects())

        if self.decide_to_reproduce():
            world.add(self.reproduce()) # (:

        if self.energy < 0:
            world.remove(self) # ):

    def change_speed(self):
        self.x_speed = max(-1, min(1, self.x_speed + random.choice((-0.1, 0.1)))) * 0.98
        self.y_speed = max(-1, min(1, self.y_speed + random.choice((-0.1, 0.1)))) * 0.98

    def move(self):
        self.x += self.x_speed * self.speed_scaler
        self.y += self.y_speed * self.speed_scaler

        self.energy -= 0.1
        print (self.energy)

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
                    self.energy += obj.size

    def decide_to_reproduce(self):
        chance_of_reproduction: float = (self.energy - 100)/100 #more likely with more excess energy
        return random.random() < chance_of_reproduction

    def reproduce(self):
        #arbitrary numbers for now
        self.energy -= 60
        return Herbivore(self.x, self.y, 40)
