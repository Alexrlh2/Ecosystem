from god import God
from worldRenderer import WorldRenderer

import pygame
import sys



# Initialize and run the simulation with graphics
god = God()
renderer = WorldRenderer(god.get_world())
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    god.update()
    renderer.draw()
    clock.tick(24)

pygame.quit()
sys.exit()

