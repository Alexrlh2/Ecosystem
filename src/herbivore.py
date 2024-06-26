import math
import random

from animal import Animal
from plant import Plant

class Herbivore(Animal):
    def __init__(self, x, y, angle: float = 0,energy=100):
        super().__init__(x, y, angle, energy)

        self.angular_momentum = random.choice((-1, 1)) # curent turn direction

    def update(self, world):
        super().update(world)

        self.try_eat(world.plants)

        if self.decide_to_reproduce():
            world.add_herbivore(self.reproduce()) # (:

        if self.energy < 0:
            world.remove(self) # ):

    def decide_movement(self):
        self.angle += (random.uniform(0, 0.2) * self.angular_momentum)

        self.angle = self.angle % (math.pi * 2)

        if random.random() < 0.1:
            self.angular_momentum *= -1

    def deplete_energy(self):
        self.energy -= 0.1

    def try_eat(self, objects):
        for obj in objects:
            if self.can_eat(obj):
                if self.collides_with(obj):
                    objects.remove(obj)
                    self.energy += obj.radius

    def can_eat(self, other):
        return type(other) is Plant

    def decide_to_reproduce(self) -> bool:
        chance_of_reproduction: float = (self.energy - 100)/100 #more likely with more excess energy
        return random.random() < chance_of_reproduction

    def reproduce(self) -> 'Herbivore':
        #arbitrary numbers for now
        self.energy -= 60
        return Herbivore(self.x, self.y, self.angle, 40)
