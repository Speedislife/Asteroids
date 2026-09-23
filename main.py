import pygame
import sys
from logger import log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0.0

    # Game loopS
    while True:
        log_state()
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()


        for draw_obj in drawable:
            draw_obj.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
