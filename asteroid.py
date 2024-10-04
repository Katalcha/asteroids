import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            first = Asteroid(self.position.x, self.position.y, radius)
            second = Asteroid(self.position.x, self.position.y, radius)
            first.velocity = self.velocity.rotate(angle) * 1.2
            second.velocity = self.velocity.rotate(angle * -1) * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
