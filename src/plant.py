from gameObject import GameObject
class Plant(GameObject):
    RADIUS = 10
    def __init__(self, x, y):
        super().__init__(x, y, self.RADIUS)
