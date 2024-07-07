from typing import List, Optional, Type

from gameObject import GameObject
from herbivore import Herbivore
from animal import Animal
from plant import Plant

import geometry_utils

import random
import math

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.plants: List[Plant] = []
        self.herbivores: List[Herbivore] = []

    def add_object(self, object: GameObject):
        object_list = self.get_objects_by_type(type(object))
        object_list.append(object)

    def get_all_objects(self):
        yield from self.plants
        yield from self.herbivores

    def get_objects_by_type(self, cls: Type[GameObject]):
        if cls == Plant:
            return self.plants
        elif cls == Herbivore:
            return self.herbivores
        else:
            return None

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

