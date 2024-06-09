from typing import List

from herbivore import Herbivore
from plant import Plant

import geometry_utils

import random
import math


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_objects = []

    def add(self, object):
        self.game_objects.append(object)

    def remove(self, object):
        if object in self.game_objects:
            self.game_objects.remove(object)

    def get_objects_near(self, position: tuple[float, float], radius: int) -> List:
        return [object for object in self.game_objects if geometry_utils.is_closer_than(position, object.pos, radius)]

    def get_objects(self):
        return self.game_objects
