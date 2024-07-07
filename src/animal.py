import math

from gameObject import GameObject
from typing import List, Tuple, Type

from brain import Brain

class Animal(GameObject):
    """Animal is a GameObject that has methods for animal stuff like moving around in the world

    Attributes:
        angle   The anticlockwise angle in radians where 0 and 2pi point to the right
        speed   The speed at which the animal is travelling in the direction it is facing where 0 is not moving, 1 is full speed, and -1 is full speed backwards"""
    
    speed_scaler = 10

    def __init__(self, x, y, brain: Brain, angle: float = 0, energy=100, radius=10):
        super().__init__(x,y, radius)

        self.angle = angle
        self.energy = energy
        self.speed = 0.5

        self.brain = brain

        # Define in inherited classes so animal can eat things
        self.edible_types: List[Type[GameObject]] = []

        self.reproduction_cost = 60
        self.baby_energy = 40

    def update(self, world):
        sensations = self.sense_environment()
        decisions = self.brain.think(sensations)

        self.decide_movement(decisions)
        self.move()

        self.deplete_energy()
        self.wrap_around_world(world.width, world.height)

        self.try_eat(world)

        if self.decide_to_reproduce(decisions):
            world.add_object(self.reproduce()) # (:

        if self.energy < 0:
            world.remove(self) # ):

    def move(self):
        dx, dy = self.get_move_vector()
        self.x, self.y = self.x + dx, self.y + dy

    def get_move_vector(self) -> Tuple[float, float]:
        return (
            (self.speed * self.speed_scaler) * math.cos(self.angle),
            (self.speed * self.speed_scaler) * math.sin(self.angle))
    
    def wrap_around_world(self, world_width, world_height):
        self.x = self.x % world_width
        self.y = self.y % world_height

    def try_eat(self, world):
        for cls in self.edible_types:
            objects = world.get_objects_by_type(cls)
            for obj in objects:
                if self.collides_with(obj):
                    objects.remove(obj)
                    self.energy += obj.radius

    def reproduce(self) -> 'Animal':
        self.energy -= self.reproduction_cost
        new_brain = self.brain.spawn()
        return self.__class__(self.x, self.y, new_brain, self.angle, self.baby_energy)

    """Implement to sense the environment, and return sensations in list format"""
    def sense_environment() -> List[float]:
        pass

    """Implement to return vector which is used to change actions and/or reproduce"""
    def think(self) -> List[float]:
        pass

    """Implement to adjust speed and direction before the animal takes its step"""
    def decide_movement(self, decisions: list):
        pass
    
    """Implement to deplete energy each update. Refer to speed to make energy depletion dependent on movement"""
    def deplete_energy(self):
        pass

    def decide_to_reproduce(self, decisions: list) -> bool:
        pass
 
