import pygame
from logger import log_state
from constants import *
from player import Player

def main() -> None:
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    # Initiate pygame and set up screen, clock, and delta time
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # Create sprite groups for batch operations
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add classes to sprite groups
    Player.containers = (updatable, drawable)

    # Create player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Main game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        # player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
