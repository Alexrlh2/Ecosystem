import math
import random

from typing import List, Type

from animal import Animal
from plant import Plant
from brain import Brain

class Herbivore(Animal):
    def __init__(self, x, y, brain: 'Brain', angle: float = 0, energy = 100):
        super().__init__(x, y, brain, angle, energy)

        self.edible_types = [Plant]
        self.angular_momentum = random.choice((-1, 1)) # current turn direction

    def sense_environment(self) -> List[float]:
        return []

    def decide_movement(self, decisions):

        angle_change = decisions[0]
        self.angle += angle_change
        self.angle = self.angle % (math.pi * 2)

        speed_change = decisions[1]
        self.speed += speed_change

    def deplete_energy(self):
        self.energy -= 0.1

    def decide_to_reproduce(self, decisions) -> bool:
        chance_of_reproduction: float = (self.energy - 100)/100 #more likely with more excess energy
        reproduction_predictor = decisions[2]
        return reproduction_predictor < chance_of_reproduction

