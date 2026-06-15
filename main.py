import pygame
from logger import log_state, log_event
from constants import *
from player import Player
from score import Score
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main() -> None:
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    # Initiate pygame and set up screen, clock, and delta time
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    font = pygame.font.Font(None, 36)

    # Create sprite groups for batch operations
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add classes to sprite groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Create player instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    score = Score()

    # Create asteroid field instance
    asteroid_field = AsteroidField()
    
    # Main game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        text_surface = font.render(f"Score: {score.current_score}", True, (255, 255, 255))
        screen.blit(text_surface, (50, 50))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    score.add_points(asteroid)
                    print(f"Score: {score.current_score}")
                    asteroid.split()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
