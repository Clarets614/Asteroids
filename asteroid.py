import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(50, 0)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, 2)
        
    def update(self, dt):
        #moves in a straight ling at a constant speed
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        
        new_velocity1 *= 1.2
        new_velocity2 *= 1.2
        
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_velocity1
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = new_velocity2
        
        
        