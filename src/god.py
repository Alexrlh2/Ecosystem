from herbivore import Herbivore
from plant import Plant
from world import World
from brain import RandomBrain

import random

class God():
    """God is responsible for initially populating the earth. God may also take responsibility
    for things such as plant reproduction until this is implemented. When plants can repopulate themselves
    there may no longer be need for a god. Time can operate through the main loop.

    I believe this is not the God Object antipattern but that's something to keep an eye on"""

    initial_herbivore_population = 50
    intial_plant_population = 100

    def __init__(self):
        self.world = self.create_world(1000, 1000)

    def create_world(self, width, height):
        world = World(width, height)

        for _ in range(self.initial_herbivore_population):
            world.add_object(Herbivore(random.randint(0, width - 1), random.randint(0, height - 1), RandomBrain()))

        for _ in range(self.intial_plant_population ):
            world.add_object(Plant(random.randint(0, width - 1), random.randint(0, height - 1)))

        return world

    def update(self):
        for obj in self.world.get_all_objects():
            obj.update(self.world)
        ##create more plants?

    def get_world(self):
        return self.world

