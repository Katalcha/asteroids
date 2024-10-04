import pygame
import sys
from constants import *
from player import Player
from shot import Shot
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
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    Player.containers = (updateable, drawable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updateable:
            sprite.update(dt)

        for asteroid in asteroids:
            if player.detectCollision(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.detectCollision(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill((0, 0, 0))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limits framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
