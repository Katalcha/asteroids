import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updateable:
            sprite.update(dt)

        for sprite in asteroids:
            if player.detectCollision(sprite):
                print("Game over!")
                sys.exit(1)

        screen.fill((0, 0, 0))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limits framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
