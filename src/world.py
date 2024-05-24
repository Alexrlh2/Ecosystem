from herbivore import Herbivore
from plant import Plant
import random
class World:
    def __init__(self, width, height, num_plants, num_herbivores):
        self.width = width
        self.height = height
        self.plants = [Plant(random.randint(0, width - 1), random.randint(0, height - 1)) for _ in range(num_plants)]
        self.herbivores = [Herbivore(random.randint(0, width - 1), random.randint(0, height - 1)) for _ in
                           range(num_herbivores)]

    def update(self):
        for herbivore in self.herbivores:
            herbivore.move(self.width, self.height)
            herbivore.eat(self.plants)