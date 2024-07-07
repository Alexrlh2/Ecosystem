import math

from gameObject import GameObject
from typing import List, Tuple, Type

class Animal(GameObject):
    """Animal is a GameObject that has methods for animal stuff like moving around in the world

    Attributes:
        angle   The anticlockwise angle in radians where 0 and 2pi point to the right
        speed   The speed at which the animal is travelling in the direction it is facing where 0 is not moving, 1 is full speed, and -1 is full speed backwards"""
    
    speed_scaler = 10

    def __init__(self, x, y, angle: float = 0,energy=100, radius=10):
        super().__init__(x,y, radius)

        self.angle = angle
        self.energy = energy
        self.speed = 0.5

        # Define in inherited classes so animal can eat things
        self.edible_types: List[Type[GameObject]] = []

    def update(self, world):
        self.decide_movement()
        self.move()
        self.deplete_energy()
        self.wrap_around_world(world.width, world.height)
        self.try_eat(world)

        if self.decide_to_reproduce():
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

    """Implement to adjust speed and direction before the animal takes its step"""
    def decide_movement(self):
        pass
    
    """Implement to deplete energy each update. Refer to speed to make energy depletion dependent on movement"""
    def deplete_energy(self):
        pass

    def decide_to_reproduce(self) -> bool:
        pass

    def reproduce(self) -> 'Animal':
        pass



 
