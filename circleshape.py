import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-class; must override
        pass

    def update(self, dt):
        # sub-class; must override
        pass

    def detectCollision(self, other):
        distance = pygame.Vector2.distance_to(self.position, other.position)
        if distance <= self.radius + other.radius:
            return True
        return False
