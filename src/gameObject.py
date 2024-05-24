class GameObject:
    def __init__(self, x, y, size=10):
        self.x = x
        self.y = y
        self.size = size

    def collidesWith(self, other):
        if (self.x < other.x + other.size and
                self.x + self.size > other.x and
                self.y < other.y + other.size and
                self.y + self.size > other.y):
            return True
        return False
