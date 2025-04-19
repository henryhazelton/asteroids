import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
       
    def draw(self, screen):
        pygame.draw.circle(screen, "white", center=self.position, radius=self.radius, width=2) # Hopefully this draws a circle correctly
        

    # Should update the display so that the asteroid travels in a straight line
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        # Firstly, should kill the asteroid and then split
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        old_radius = self.radius
        random_angle = random.uniform(20, 50) # Create a random angle between 20 & 50 degrees that the new asteroids will split at

        # The new velocity vectors for the asteroids 
        asteroid_1_velocity_vector = self.velocity.rotate(random_angle)
        asteroid_2_velocity_vector = self.velocity.rotate(-random_angle)

        # Working out the size of the new asteroids
        radius_asteroid_1 = old_radius - ASTEROID_MIN_RADIUS
        radius_asteroid_2 = old_radius - ASTEROID_MIN_RADIUS

        # Create the two new asteroid objects
        asteroid_1 = Asteroid(self.position.x, self.position.y, radius=radius_asteroid_1)
        asteroid_2 = Asteroid(self.position.x, self.position.y, radius=radius_asteroid_2)

        # Setting the new asteroids velocities
        asteroid_1.velocity = asteroid_1_velocity_vector * 1.2
        asteroid_2.velocity = asteroid_2_velocity_vector
        