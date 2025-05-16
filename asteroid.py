import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def _init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

# Override the update() method so that it moves in a straight line at constant speed.
# On each frame, it should add (self.velocity * dt) to its position
# (get self.velocity from its parent class, CircleShape).

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        # Spawn Vector new asteroid
        a = self.velocity.rotate(random_angle)
        # Spawn Vector new asteroid
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
