import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        # left
        if keys[pygame.K_a]:
            self.rotate(-delta_time)        
        # right
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        # up
        if keys[pygame.K_w]:
            self.move(delta_time)
        # down
        if keys[pygame.K_s]:
            self.move(-delta_time)
        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot()            
        
    def draw(self, screen):
        pygame.draw.polygon(screen, color=(255,255,255), points=self.triangle(), width=2)
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time
        
    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time
        
    def shoot(self):
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        