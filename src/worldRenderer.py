import world

import pygame


class WorldRenderer:
    SCALE = 1
    BACKGROUND_COLOUR = (110, 86, 58)

    def __init__(self, world):

        self.world = world

        pygame.init()
        self.screen = pygame.display.set_mode((world.width * self.SCALE, world.height * self.SCALE))
        pygame.display.set_caption("Ecosystem Simulation")

    def _draw_world(self):
        self._draw_background()
        self._draw_entities()

    def _draw_background(self):
        self.screen.fill(self.BACKGROUND_COLOUR)

    def _draw_entities(self):
        for plant in self.world.plants:
            rect = pygame.Rect(plant.x, plant.y, plant.SIZE, plant.SIZE)
            pygame.draw.rect(self.screen, (0, 255, 0), rect)

        for herbivore in self.world.herbivores:
            rect = pygame.Rect(herbivore.x, herbivore.y, herbivore.size, herbivore.size)
            pygame.draw.rect(self.screen, (0, 0, 255), rect)

    def draw(self):
        self._draw_world()
        pygame.display.flip()



