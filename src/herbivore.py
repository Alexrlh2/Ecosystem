import random

from gameObject import GameObject


class Herbivore(GameObject):
    def move(self, world_width, world_height):
        self.x = (self.x + random.choice([-1, 0, 1])) % world_width
        self.y = (self.y + random.choice([-1, 0, 1])) % world_height

    def eat(self, plants):
        for plant in plants:
            if self.collidesWith(plant):
                plants.remove(plant)
                return True
        return False
