from herbivore import Herbivore
from plant import Plant

import random
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_objects = []

    def add(self, object):
        self.game_objects.append(object) #i think eventually we wont need separate lists it'll just be game objects

    def get_objects(self):
        return self.game_objects

