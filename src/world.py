from herbivore import Herbivore
from plant import Plant

import random
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.plants = []
        self.herbivores = []

    def add_plant(self, plant):
        self.plants.append(plant) #i think eventually we wont need separate lists it'll just be game objects

    def add_herbivore(self, herbivore):
        self.herbivores.append(herbivore)
    def update(self):
        for herbivore in self.herbivores:
            herbivore.update(self.width, self.height)
            herbivore.eat(self.plants)

