import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Create two smaller asteroids
        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate (random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_vector1 * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_vector2 * 1.2

        
    def draw(self, screen):    
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt
        
         
