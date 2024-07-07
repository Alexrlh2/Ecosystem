import random
import copy

class Brain:

    """ Implement to store any memories or brain circuits"""
    def __init__(self) -> None:
        pass

    """ I chose the name because I like how it sounds"""
    def spawn(self) -> 'Brain':
        new_brain = copy.deepcopy(self)
        new_brain.mutate()
        return new_brain

    """ Implement to return a set of decisions based on a set of input, or sensations"""
    def think(self, sensations: list) -> list:
        pass

    """ Implement to update brain circuits during reproduction"""
    def mutate(self):
        pass


class RandomBrain(Brain):
    """ The random brain does not mutate, or remember anything"""

    def think(self, sensations: list) -> list:
        decisions = []
        
        # angle change
        decisions.append(random.uniform(-0.2, 0.2))

        # speed change
        decisions.append(0)

        # predictor for reproduction
        decisions.append(random.random())

        return decisions
