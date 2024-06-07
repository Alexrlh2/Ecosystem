from plant import Plant
from herbivore import Herbivore

import math
import pygame


class WorldRenderer:
    """Renders a world and all its GameObjects

    Warning - Pygame uses (0,0) = topleft and angles go anticlockwise. Hide away all the disgusting dealing with that in this class"""

    SCALE = 1
    BACKGROUND_COLOUR = (224, 208, 162)

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
    def _draw_plant(self, plant: Plant) -> None:
        green = (78, 125, 67)
        pygame.draw.circle(self.screen, green, (plant.x, plant.y), plant.radius)

    def _draw_herbivore(self, herbivore: Herbivore) -> None:
        brown = (153, 112, 58)
        cream = (250, 239, 225)
        pygame.draw.circle(self.screen, brown, (herbivore.x, herbivore.y), herbivore.radius)
        self._draw_arrow(cream, (herbivore.x, herbivore.y), herbivore.radius, herbivore.angle)

    def _draw_arrow(self, color: tuple[int, int, int], start_pos: tuple[int, int], length: int, bearing: float, width: int = 1) -> None:
        """
        :param color: The color of the arrow.
        :param start_pos: The starting position (tail) of the arrow as a tuple (x, y).
        :param length: The length of the arrow.
        :param bearing_degrees: The direction of the arrow in degrees (0 or 360 is up, 90 is right).
        :param width: The width of the arrow's shaft.
        """

        angle = math.pi / 2 - bearing

        end_pos = (start_pos[0] + length * math.cos(angle),
                   start_pos[1] + length * math.sin(angle))

        # Draw the arrow shaft
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

        head_length = 4
        head_width = 4
        # Calculate the points for the arrow head
        left_point = (end_pos[0] - head_length * math.cos(angle - math.pi / 6),
                      end_pos[1] - head_length * math.sin(angle - math.pi / 6))
        right_point = (end_pos[0] - head_length * math.cos(angle + math.pi / 6),
                       end_pos[1] - head_length * math.sin(angle + math.pi / 6))

        # Draw the arrow head
        pygame.draw.polygon(self.screen, color, [end_pos, left_point, right_point])
    def draw(self):
        self._draw_world()
        pygame.display.flip()




