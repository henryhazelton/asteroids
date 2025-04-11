import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
       
    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius, width=2) # Hopefully this draws a circle correctly
        

    # Should update the display so that the asteroid travels in a straight line
    def update(self, dt):
        self.position += self.velocity * dt
        
