# Class for shooting

import pygame

from constants import SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=SHOT_RADIUS, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt