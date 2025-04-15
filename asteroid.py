from circleshape import CircleShape
import pygame
import random
from groups import updatables, drawables, asteroids
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = (asteroids, updatables, drawables)
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        # Always destroy the current asteroid
        self.kill()
        
        # If this is a small asteroid, we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # Calculate new properties for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors at opposite angles
        vel1 = self.velocity.rotate(split_angle) * 1.2
        vel2 = self.velocity.rotate(-split_angle) * 1.2
        
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2

