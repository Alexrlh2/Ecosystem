import math
import random

from animal import Animal
from plant import Plant

class Herbivore(Animal):
    def __init__(self, x, y, angle: float = 0,energy=100):
        super().__init__(x, y, angle, energy)

        self.edible_types = [Plant]
        self.angular_momentum = random.choice((-1, 1)) # current turn direction

    def decide_movement(self):
        self.angle += (random.uniform(0, 0.2) * self.angular_momentum)

        self.angle = self.angle % (math.pi * 2)

        if random.random() < 0.1:
            self.angular_momentum *= -1

    def deplete_energy(self):
        self.energy -= 0.1

    def decide_to_reproduce(self) -> bool:
        chance_of_reproduction: float = (self.energy - 100)/100 #more likely with more excess energy
        return random.random() < chance_of_reproduction

    def reproduce(self) -> 'Herbivore':
        #arbitrary numbers for now
        self.energy -= 60
        return Herbivore(self.x, self.y, self.angle, 40)
