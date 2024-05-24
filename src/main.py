from herbivore import Herbivore
from plant import Plant
from world import World
from worldRenderer import WorldRenderer

import pygame
import sys


# Initialize and run the simulation with graphics
world = World(100, 100, 20, 5)
renderer = WorldRenderer(world)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.update()
    renderer.draw()
    clock.tick(5)

pygame.quit()
sys.exit()

