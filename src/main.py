from herbivore import Herbivore
from plant import Plant
from world import World
from worldRenderer import WorldRenderer

# Initialize and run the simulation with graphics
world = World(100, 100, 20, 5)
renderer = WorldRenderer(world)
renderer.run()


