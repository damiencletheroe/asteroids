from circleshape import CircleShape
import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width = LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one_vector = self.velocity.rotate(angle)
            asteroid_two_vector = self.velocity.rotate(-angle)
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = asteroid_one_vector * 1.2
            asteroid_two.velocity = asteroid_two_vector * 1.2


        


