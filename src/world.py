from typing import List, Optional

from herbivore import Herbivore
from plant import Plant

import geometry_utils

import random
import math

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.plants = []
        self.herbivores = []

    def add_plant(self, plant: Plant):
        self.plants.append(plant)

    def add_herbivore(self, herbivore: Herbivore):
        self.herbivores.append(herbivore)

    def get_all_objects(self):
        yield from self.plants
        yield from self.herbivores

    def remove(self, object):
        if object in self.plants:
            self.plants.remove(object)
        if object in self.herbivores:
            self.herbivores.remove(object)

    def get_nearest_plant(self, pos: tuple[float, float]) -> Optional[Plant]:
        nearest_plant = None
        for plant in self.plants:
            if (
                (not nearest_plant) or
                (geometry_utils.is_closer_than(pos, plant.pos, geometry_utils.get_distance_between(pos, nearest_plant.pos)))
            ):
                nearest_plant = plant
        return nearest_plant

    def get_objects_near(self, position: tuple[float, float], radius: int) -> List:
        return [object for object in self.get_all_objects() if
                geometry_utils.is_closer_than(position, object.pos, radius)]

