from plant import Plant
from herbivore import Herbivore

import pygame


class WorldRenderer:
    SCALE = 1
    BACKGROUND_COLOUR = (110, 86, 58)

    def __init__(self, world):

        self.world = world

        pygame.init()
        self.screen = pygame.display.set_mode((world.width * self.SCALE, world.height * self.SCALE))
        pygame.display.set_caption("Ecosystem Simulation")

        self.render_functions = {
            Plant: self._draw_plant,
            Herbivore: self._draw_herbivore
        }

    def _draw_world(self):
        self._draw_background()
        self._draw_entities()

    def _draw_background(self):
        self.screen.fill(self.BACKGROUND_COLOUR)

    def _draw_entities(self):
        for obj in self.world.get_objects():
            render_function = self.render_functions.get(type(obj), None)
            if render_function:
                render_function(obj)
            else:
                print(f"No render function for object of type {type(obj)}")
    def _draw_plant(self, plant):
        rect = pygame.Rect(plant.x, plant.y, plant.size, plant.size)
        pygame.draw.rect(self.screen, (0, 255, 0), rect)

    def _draw_herbivore(self, herbivore):
        rect = pygame.Rect(herbivore.x, herbivore.y, herbivore.size, herbivore.size)
        pygame.draw.rect(self.screen, (0, 0, 255), rect)

    def draw(self):
        self._draw_world()
        pygame.display.flip()



