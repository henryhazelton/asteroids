# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame  # type: ignore
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    # Initalisation code
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Making containers to hold the objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Setting the containers to the classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    asteroid_field = AsteroidField()

    # The Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteriod in asteroids:
            if asteriod.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteriod.collides_with(shot):
                    shot.kill()
                    asteriod.split()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limits the FPS to 60


if __name__ == "__main__":
    main()
