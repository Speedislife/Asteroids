import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
# or import everything: from module_name import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0.0

    # Game loop
    while True:
        log_state()
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
