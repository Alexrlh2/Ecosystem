import random
class Herbivore:
    def __init__(self, x, y, size = 10):
        self.x = x
        self.y = y
        self.size = size

    def move(self, world_width, world_height):
        self.x = (self.x + random.choice([-1, 0, 1])) % world_width
        self.y = (self.y + random.choice([-1, 0, 1])) % world_height

    def eat(self, plants):
        for plant in plants:
            if self.x == plant.x and self.y == plant.y:
                plants.remove(plant)
                return True
        return False